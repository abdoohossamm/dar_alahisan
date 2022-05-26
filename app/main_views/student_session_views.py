from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Day,Room, Teacher, Session, StudentSessions, Student
from ..forms import TeacherForm,StudentSessionsForm
from ..functions import day_in_arabic
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
from ..functions import check_suc_url


class StudentSessionCreate(LoginRequiredMixin,CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('session')
    type='طالب بالنسبة لحلقة'
    form = StudentSessionsForm

class StudentSessionsCreateByDay(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = ''
    type="طالب بالنسبة لحلقة"
    form = StudentSessionsForm
    initial = {}
    def get(self, request, day=None, teacher=None, next='', **initial):
        for k, v in initial.items():
            self.initial[k] = [v]
        self.success_url = check_suc_url(next, self.success_url)
        ctx = {
            'form': self.form(initial=self.initial, day=day, teacher=teacher),
            'suc_url': self.success_url,
            'type': self.type
            }
        return render(request, self.template, ctx)

class StudentSessionDelete(LoginRequiredMixin,CRUDDelete):
    model = StudentSessions
    success_url = reverse_lazy('session')
    template = 'make_confirm_delete.html'
    type = 'طالب بالنسبة لحلقة'

class StudentSessionUpdate(LoginRequiredMixin,CRUDUpdate):
    model = StudentSessions
    success_url = reverse_lazy('session')
    form = StudentSessionsForm
    template = 'add_update_form.html'
    type = 'طالب بالنسبة لحلقة'
