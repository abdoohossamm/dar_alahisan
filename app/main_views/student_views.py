from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Student, StudentSessions,Day,Session
from ..forms import StudentForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete  # type: ignore
from django.db.models import Q
from django.core.paginator import Paginator
from ..functions import ITEM_PER_PAGE

'''
Functions for view.
does not return web request or response.
'''
def search_model(request, item:int=10):
    strval =  request.GET.get("search", False)
    page_number = request.GET.get('page')

    if strval :
        query = Q(name__icontains=strval) 
        query.add(Q(n_id__icontains=strval), Q.OR)
        query.add(Q(pk__icontains=strval), Q.OR)
        query.add(Q(address__icontains=strval), Q.OR)
        query.add(Q(phone__icontains=strval), Q.OR)
        query.add(Q(home_number__icontains=strval), Q.OR)
        student = Student.objects.filter(query).select_related()
        return {
            'search': strval,
            'students': student,
            'page_obj': student
        }
    else :
        student = Student.objects.all()
        paginator = Paginator(student, item)
        page_obj = paginator.get_page(page_number)
        return {
        'search': strval,
        'students': student,
        'page_obj': page_obj
        }

'''
Student views
4 views for detials, create, update and delete
'''
class StudentView(LoginRequiredMixin,View):
    template = 'student/student.html'
    form = StudentForm
    success_url = reverse_lazy('student')
    type = 'طالب'
    def get(self, request):
        search = search_model(request, ITEM_PER_PAGE)
        ctx = {
            'students': search['students'],
            'search': search['search'],
            'page_obj': search['page_obj'],
            'form': self.form(),
            'suc_url': self.success_url,
            'type':self.type,
            'search_bar': True
            }
        return render(request, self.template, ctx)
    def post(self, request):
        form = self.form(request.POST)
        search = search_model(request, ITEM_PER_PAGE)
        
        if not form.is_valid():
            ctx = {
                'students': search['students'],
                'search': search['search'],
                'page_obj': search['page_obj'],
                'form': form,
                'suc_url': self.success_url,
                'type':self.type,
                'search_bar': True

                }
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)

class StudentDetailsView(LoginRequiredMixin, View):
    template = 'student/student_details.html'
    model = Student
    def get(self, request, pk):
        student = get_object_or_404(self.model, pk=pk)
        student_session = StudentSessions.objects.filter(student=student)
        session = Session.objects.filter(student_session__student=student)
        for se in session:
            print(se)
        days = Day.objects.all().order_by('id')
        success_url = reverse_lazy('student_details', kwargs={'pk':student.pk})
        ctx = {
            'student': student,
            'student_session': student_session,
            'days': days,
            'suc_url': success_url
            }
        return render(request, self.template, ctx)






'''
CRUD Views
'''
class StudentCreate(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('student')
    type='طالب'
    form = StudentForm
class StudentUpdate(LoginRequiredMixin, CRUDUpdate):
    model = Student
    success_url = reverse_lazy('student')
    template = 'add_update_form.html'
    form = StudentForm
    type='طالب'
class StudentDelete(LoginRequiredMixin, CRUDDelete):
    model = Student
    success_url = reverse_lazy('student')
    form = StudentForm
    template = 'make_confirm_delete.html'
    type = 'طالب'
