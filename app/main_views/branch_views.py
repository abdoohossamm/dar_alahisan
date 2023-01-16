from ..models import Branch
from ..forms import BranchForm
from  .session_views import search_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from ..models import Session
from ..forms import SessionForm
from ..filters import SessionFilter
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
from django.db.models import Q
from django.core.paginator import Paginator
from ..functions import ITEM_PER_PAGE

'''
Branch views
4 views for detials, create, update and delete
'''
def search_model(request, branch, item:int=10):
    strval =  request.GET.get("search", False)
    page_number = request.GET.get('page')
    if strval :
        query = Q(day__day__icontains=strval)
        query.add(Q(name__branch=branch))
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
        print("filter")
        session = Session.objects.filter(name__branch=branch).select_related('name', 'teacher','day').order_by('day')
        myfilter = SessionFilter(request.GET, queryset=session)
        session = myfilter.qs
        return {
                'search': strval,
                'sessions': session,
                'page_obj': session,
                'filter': myfilter,
                }
    else:
        session = Session.objects.filter(name__branch=branch).select_related('name', 'teacher','day').order_by('day')
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

class BranchView(LoginRequiredMixin,View):
    template = 'branch/branch.html'
    form = BranchForm
    success_url = reverse_lazy('branch')
    type='فرع'
    def get(self, request):
        branch = Branch.objects.all()
        ctx = {
            'branches': branch,
            'form': self.form(),
            'suc_url': self.success_url,
            'type': self.type
            }
        return render(request, self.template, ctx)
    def post(self, request):
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

class BranchSessionView(LoginRequiredMixin, View):
    template = 'branch/branch_session_detail.html'
    success_url = reverse_lazy('session')
    form = SessionForm
    type = 'حلقة'
    myfilter = SessionFilter

    def get(self, request, branch, next=''):
        search = search_model(request, branch, ITEM_PER_PAGE)
        branch = Branch.objects.get(pk=branch)
        ctx = {
            'sessions': search['sessions'],
            'search': search['search'],
            'page_obj': search['page_obj'],
            'form': self.form(),
            'type': self.type,
            'filter': search['filter'],
            'search_bar': True,
            'suc_url': self.success_url,
            'branch': branch,
        }
        return render(request, self.template, ctx)

    def post(self, request, branch):
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
                'type': self.type,
                'search_bar': True

            }
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)


'''
CRUD views
'''
class BranchCreate(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('branch')
    type='فرع'
    form = BranchForm
class BranchUpdate(LoginRequiredMixin, CRUDUpdate):
    model = Branch
    success_url = reverse_lazy('branch')
    template = 'add_update_form.html'
    form = BranchForm
    type='فرع'
class BranchDelete(LoginRequiredMixin, CRUDDelete):
    model = Branch
    success_url = reverse_lazy('branch')
    form = BranchForm
    template = 'make_confirm_delete.html'
    type = 'فرع'