from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Session, StudentSessions
from ..forms import SessionForm, StudentSessionsForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
from ..functions import check_suc_url
from django.db.models import Q

    
'''
Session views
4 views for detials, create, update and delete
'''
class SessionView(LoginRequiredMixin,View):
    template = 'session/session.html'
    success_url = reverse_lazy('session')
    def get(self, request,next=''):
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(day__day__icontains=strval) 
            query.add(Q(pk__icontains=strval), Q.OR)
            query.add(Q(time__icontains=strval), Q.OR)
            query.add(Q(name__name__icontains=strval), Q.OR)
            query.add(Q(teacher__name__icontains=strval), Q.OR)
            session = Session.objects.filter(query).select_related().order_by('day')
        else :
            session = Session.objects.all().order_by('day')
        student_sessions = StudentSessions.objects.all()
        ctx = {
            'sessions': session,
            'search': strval,
            'suc_url': self.success_url,
            'student_sessions': student_sessions,
            'search_bar': True
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
