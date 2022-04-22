from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Manager
from ..forms import ManagerForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
from django.db.models import Q
from django.core.paginator import Paginator
from ..functions import ITEM_PER_PAGE

'''
Manager views
4 views for detials, create, update and delete
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
        manager = Manager.objects.filter(query).select_related()
        return {
        'search': strval,
        'managers': manager,
        'page_obj': manager
        }
    else :
        manager = Manager.objects.all()
    paginator = Paginator(manager, item) # Show 25 contacts per page.
    page_obj = paginator.get_page(page_number)
    return {
            'search': strval,
            'managers': manager,
            'page_obj': page_obj
            }

class ManagerDetailsView(LoginRequiredMixin,View):
    template = 'manager/manager_details.html'
    success_url = reverse_lazy('manager')
    type = 'موظف'
    form = ManagerForm
    def get(self, request):
        search = search_model(request, ITEM_PER_PAGE)
        ctx = {
            'managers': search['managers'],
            'search': search['search'],
            'page_obj': search['page_obj'],
            'form': self.form(),
            'type':self.type,
            'search_bar': True
            }
        return render(request, self.template, ctx)
    
    def post(self, request):
        form = self.form(request.POST)
        search = search_model(request, ITEM_PER_PAGE)
        if not form.is_valid():
            ctx = {
                'managers': search['managers'],
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
class ManagerCreate(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('manager')
    type='موظف'
    form = ManagerForm
class ManagerUpdate(LoginRequiredMixin, CRUDUpdate):
    model = Manager
    success_url = reverse_lazy('manager')
    template = 'add_update_form.html'
    form = ManagerForm
    type='موظف'
class ManagerDelete(LoginRequiredMixin, CRUDDelete):
    model = Manager
    success_url = reverse_lazy('manager')
    form = ManagerForm
    template = 'make_confirm_delete.html'
    type = 'موظف'


# class ManagerCreate(View):
#     template = 'add_update_form.html'
#     success_url = reverse_lazy('manager')

#     def get(self, request):
#         form = ManagerForm()
#         ctx = {
#                 'form': form,
#                 'type': 'موظف',
#                 'suc_url': self.success_url,
#                 }
#         return render(request, self.template, ctx)

#     def post(self, request):
#         form = ManagerForm(request.POST)
#         print(request.POST)
#         if not form.is_valid():
#             ctx = {
#                 'form': form,
#                 'type': 'موظف',
#                 'suc_url': self.success_url,
#                 }
#             return render(request, self.template, ctx)
#         form.save()
#         try:
#             if request.POST['add_another'] == 'on':
#                 ctx = {
#                         'form': ManagerForm(
#                             initial={
#                                 'add_another': 'on'
#                                 }
#                             ),
#                         'suc_url': self.success_url,
#                         'type':'محفظ'
#                         }
#                 return render(request, self.template, ctx)
#         except:
#             pass
#         return redirect(self.success_url)
    

# class ManagerUpdate(View):
#     model = Manager
#     success_url = reverse_lazy('manager')
#     template = 'add_update_form.html'

#     def get(self, request, pk):
#         manager = get_object_or_404(self.model, pk=pk)
#         form = ManagerForm(instance=manager)
#         ctx = {
#             'form': form,
#             'type': 'موظف',
#             'suc_url': self.success_url,
#             'update': True
#             }
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         manager = get_object_or_404(self.model, pk=pk)
#         form = ManagerForm(request.POST, instance=manager)
#         if not form.is_valid():
#             ctx = {
#                 'form': form,
#                 'type': 'موظف',
#                 'suc_url': self.success_url,
#                 'update': True
#                 }
#             return render(request, self.template, ctx)
#         form.save()
#         return redirect(self.success_url)

# class ManagerDelete(View):
#     model = Manager
#     success_url = reverse_lazy('manager')
#     template = 'make_confirm_delete.html'

#     def get(self, request, pk):
#         manager = get_object_or_404(self.model, pk=pk)
#         form = ManagerForm(instance=manager)
#         ctx = {'model': manager, 'type': 'موظف', 'suc_url':self.success_url }
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         make.delete()
#         return redirect(self.success_url)
