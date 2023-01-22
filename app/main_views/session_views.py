from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Session, StudentSessions
from ..forms import SessionForm, StudentSessionsForm
from ..filters import SessionFilter
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
from ..functions import check_suc_url
from django.db.models import Q
from django.core.paginator import Paginator
from ..functions import ITEM_PER_PAGE
from django.contrib.auth.decorators import login_required


'''
Functions for view.
does not return web request or response.
'''
def search_model(request, item:int=10):
    strval =  request.GET.get("search", False)
    page_number = request.GET.get('page')
    if strval :
        query = Q(day__day__icontains=strval)
        query.add(Q(pk__icontains=strval), Q.OR)
        query.add(Q(time__icontains=strval), Q.OR)
        query.add(Q(name__name__icontains=strval), Q.OR)
        query.add(Q(teacher__name__icontains=strval), Q.OR)
        session = Session.objects.filter(query).select_related('name', 'teacher','day').order_by('day')
        myfilter = SessionFilter(request.GET, queryset=session)
        return {
            'search': strval,
            'sessions': session,
            'page_obj': session,
            'filter': myfilter,
        }
    elif request.GET.get("day", False) or request.GET.get("time", False) or request.GET.get("name", False) or request.GET.get("teacher", False) or request.GET.get("branch", False):
        session = Session.objects.all().select_related('name', 'teacher','day').order_by('day')
        myfilter = SessionFilter(request.GET, queryset=session)
        session = myfilter.qs
        return {
                'search': strval,
                'sessions': session,
                'page_obj': session,
                'filter': myfilter,
                }
    else:
        session = Session.objects.all().select_related('name', 'teacher','day').order_by('day')
        myfilter = SessionFilter(request.GET, queryset=session)
        session = myfilter.qs
        paginator = Paginator(session, item) # Show 25 contacts per page.
        page_obj = paginator.get_page(page_number)
        return {
                'search': strval,
                'sessions': session,
                'page_obj': page_obj,
                'filter': myfilter,
                }

'''
Session views
4 views for detials, create, update and delete
'''

class SessionView(LoginRequiredMixin,View):
    template = 'session/session.html'
    success_url = reverse_lazy('session')
    form = SessionForm
    type = 'حلقة'
    myfilter = SessionFilter
    def get(self, request,next=''):
        search = search_model(request, ITEM_PER_PAGE)

        
        ctx = {
            'sessions': search['sessions'],
            'search': search['search'],
            'page_obj':search['page_obj'],
            'form': self.form(),
            'type':self.type,
            'filter': search['filter'],
            'search_bar': True,
            'suc_url': self.success_url,
            }
        return render(request, self.template, ctx)
    
    def post(self, request):
        form = self.form(request.POST)
        search = search_model(request, ITEM_PER_PAGE)
        if not form.is_valid():
            ctx = {
                'sessions': search['sessions'],
                'search': search['search'],
                'page_obj': search['page_obj'],
                'form': form,
                'filter': search['filter'],
                'suc_url': self.success_url,
                'type':self.type,
                'search_bar': True

                }
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)

@login_required
def students_in_session(request, pk):
    template = 'session/students_in_session.html'
    session = get_object_or_404(Session.objects.all().select_related('teacher', 'day', 'name'), pk=pk)
    form = StudentSessionsForm(initial={'session':session})
    student_session = StudentSessions.objects.filter(session=session).select_related('student')
    success_url = reverse_lazy('students_in_session', kwargs={'pk':session.pk})
    ctx ={
        'session': session,
        'student_session': student_session,
        'suc_url': success_url,
        'form': form,
        }
    # POST Request
    if request.method == 'POST':
        form = StudentSessionsForm(request.POST)
        if not form.is_valid():
            ctx ['form']= form
            return render(request, template, ctx)
        form.save()
        return redirect(success_url)
    return render(request, template, ctx)

    
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
