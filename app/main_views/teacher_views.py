from webbrowser import get
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Teacher, Session, Day, StudentSessions
from ..forms import TeacherForm, SessionForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
'''
Teacher views
'''    
class TeachersView(LoginRequiredMixin, View):
    template = 'teacher/teacher.html'
    def get(self, request):
        teacher = Teacher.objects.all()
        ctx = {'teachers': teacher}
        return render(request, self.template, ctx)


class TeacherDetailsView(LoginRequiredMixin, View):
    template = 'teacher/teacher_details.html'
    model = Teacher
    def get(self, request, pk):
        teacher = get_object_or_404(self.model, pk=pk)
        session_ = Session.objects.filter(teacher=pk)
        days = Day.objects.all().order_by('id')
        success_url = reverse_lazy('teacher_details', kwargs={'pk':teacher.pk})
        ctx = {
            'teacher': teacher,
            'session': session_,
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


