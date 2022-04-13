from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Day,Room, Teacher, Session, StudentSessions, Student
from .forms import TeacherForm,StudentSessionsForm
from .functions import day_in_arabic


class StudentSessionCreate(View):
    template = 'add_update_form.html'
    success_url = reverse_lazy('session')
    type='طالب بالنسبة لحلقة'
    form = StudentSessionsForm
    student = ''
    session = ''
    initial = {
            'student': student,
            'session': session
               }
    
    def get(self, request, student_pk=None, session_pk=None):
        self.initial['student'] = student_pk
        self.initial['session'] = session_pk
        ctx = {
            'form': self.form(initial=self.initial),
            'suc_url': self.success_url,
            'type': self.type
            }
        return render(request, self.template, ctx)


    def post(self, request, student_pk=None, session_pk=None):
        form = self.form(request.POST)

        print(request.POST)
        if not form.is_valid():
            ctx = {
                'form': form,
                'suc_url': self.success_url,
                'type':self.type
                }
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)


class DaysView(LoginRequiredMixin, View):
    template = 'days.html'
    day = Day.objects.all()
    def get(self, request):
        ctx = {
            'days': self.day,
        }
        return render(request, self.template,ctx)

class MainView(LoginRequiredMixin, View):
    template = 'today.html'
    day_name = day_in_arabic()[0]
    day_id = Day.objects.get(day=day_name)
    session = Session.objects.all().order_by('time')
    session_today = Session.objects.filter(day=day_id).order_by('time')
    teacher = Teacher.objects.all()
    student_counter = 0
    teachers=[]
    for i in session.filter(day=day_id):
        student_count = StudentSessions.objects.filter(session= i).count()
        student_counter += student_count
    for teach in teacher:
        for i in session_today:
            if session_today.filter(teacher=teach) and teach not in teachers: 
                teachers.append(teach)
    def get(self, request):
        ctx = {
            'day_name': self.day_name,
            'sessions': self.session_today,
            'student_count': self.student_counter,
            'teacher_count': len(self.teachers)
        }
        return render(request, self.template,ctx)

