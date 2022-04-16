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