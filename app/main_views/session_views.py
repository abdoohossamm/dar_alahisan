from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Session, StudentSessions
from ..forms import SessionForm, StudentSessionsForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
from ..functions import check_suc_url

    
'''
Session views
4 views for detials, create, update and delete
'''
class SessionView(LoginRequiredMixin,View):
    template = 'session/session.html'
    success_url = reverse_lazy('session')
    def get(self, request,next=''):
        session = Session.objects.all().order_by('day')
        student_sessions = StudentSessions.objects.all()
        ctx = {
            'sessions': session,
            'suc_url': self.success_url,
            'student_sessions': student_sessions,
            }
        return render(request, self.template, ctx)


'''
CRUD Views
'''
class SessionCreate(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('session')
    type='حلقه'
    form = SessionForm
class SessionUpdate(LoginRequiredMixin, CRUDUpdate):
    model = Session
    success_url = reverse_lazy('session')
    template = 'add_update_form.html'
    form = SessionForm
    type='حلقه'
class SessionDelete(LoginRequiredMixin, CRUDDelete):
    model = Session
    success_url = reverse_lazy('session')
    form = SessionForm
    template = 'make_confirm_delete.html'
    type = 'حلقه'
