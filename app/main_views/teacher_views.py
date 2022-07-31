from webbrowser import get
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Teacher, Session, Day, StudentSessions
from ..forms import TeacherForm, SessionForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
from django.db.models import Q
from django.core.paginator import Paginator
from ..functions import ITEM_PER_PAGE

'''
Teacher views
'''    
def search_model(request, item:int=10):
    strval =  request.GET.get('search', False)
    page_number = request.GET.get('page')
    if strval :
        query = Q(name__icontains=strval) 
        query.add(Q(n_id__icontains=strval), Q.OR)
        query.add(Q(pk__icontains=strval), Q.OR)
        query.add(Q(address__icontains=strval), Q.OR)
        query.add(Q(phone__icontains=strval), Q.OR)
        query.add(Q(home_number__icontains=strval), Q.OR)
        teacher = Teacher.objects.filter(query)
        return {
            'search': strval,
            'teachers': teacher,
            'page_obj': teacher
        }
    else :
        teacher = Teacher.objects.all()
    paginator = Paginator(teacher, item)
    page_obj = paginator.get_page(page_number)
    return {
            'search': strval,
            'teachers': teacher,
            'page_obj': page_obj
            }


class TeachersView(LoginRequiredMixin, View):
    template = 'teacher/teacher.html'
    form = TeacherForm
    success_url = reverse_lazy('teacher')
    type = 'محفظ'

    def get(self, request):
        search = search_model(request, ITEM_PER_PAGE)
        ctx = {
            'teachers': search['teachers'],
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
                'teachers': search['teachers'],
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

class TeacherDetailsView(LoginRequiredMixin, View):
    template = 'teacher/teacher_details.html'
    model = Teacher
    def get(self, request, pk):
        teacher = get_object_or_404(self.model, pk=pk)
        session = Session.objects.filter(teacher=pk).select_related('session', 'sessions')
        days = Day.objects.all().order_by('id')
        success_url = reverse_lazy('teacher_details', kwargs={'pk':teacher.pk})
        ctx = {
            'teacher': teacher,
            'session': session,
            'days': days,
            'suc_url': success_url
            }
        return render(request, self.template, ctx)



'''
CRUD Views
'''
class TeacherCreate(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('teacher')
    type="محفظ"
    form = TeacherForm
    
    
class TeacherUpdate(LoginRequiredMixin, CRUDUpdate):
    model = Teacher
    success_url = reverse_lazy('teacher')
    template = 'add_update_form.html'
    form = TeacherForm
    type="محفظ"
    
    
class TeacherDelete(LoginRequiredMixin, CRUDDelete):
    model = Teacher
    success_url = reverse_lazy('teacher')
    form = TeacherForm
    template = 'make_confirm_delete.html'
    type = 'محفظ'


