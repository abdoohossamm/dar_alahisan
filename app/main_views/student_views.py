from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Student, StudentSessions,Day,Session
from ..forms import StudentForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete  # type: ignore

'''
Student views
4 views for detials, create, update and delete
'''
class StudentView(LoginRequiredMixin,View):
    template = 'student/student.html'
    def get(self, request):
        student = Student.objects.all()
        ctx = {
            'students': student
            }
        return render(request, self.template, ctx)

class StudentDetailsView(LoginRequiredMixin, View):
    template = 'student/student_details.html'
    model = Student
    def get(self, request, pk):
        student = get_object_or_404(self.model, pk=pk)
        student_session = StudentSessions.objects.filter(student=student)
        session = Session.objects.filter(student_session__student=student)
        for se in session:
            print(se)
        days = Day.objects.all()
        success_url = reverse_lazy('student_details', kwargs={'pk':student.pk})
        ctx = {
            'student': student,
            'student_session': student_session,
            'days': days,
            'suc_url': success_url
            }
        return render(request, self.template, ctx)


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
