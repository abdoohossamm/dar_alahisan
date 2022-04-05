from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Session, StudentSessions
from ..forms import SessionForm, StudentSessionsForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete

    
'''
Session views
4 views for detials, create, update and delete
'''
class SessionView(LoginRequiredMixin,View):
    template = 'session/session.html'
    def get(self, request):
        session = Session.objects.all().order_by('day')
        student_sessions = StudentSessions.objects.all()
        ctx = {
            'sessions': session,
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

# class SessionCreate(View):
#     template = 'add_update_form.html'
#     success_url = reverse_lazy('session')

#     def get(self, request):
#         form = SessionForm()
#         ctx = {
#                 'form': form,
#                 'type': 'حلقه',
#                 'suc_url': self.success_url,
#                 }
#         return render(request, self.template, ctx)

#     def post(self, request):
#         form = SessionForm(request.POST)
#         print(request.POST)
#         if not form.is_valid():
#             ctx = {
#                 'form': form,
#                 'type': 'حلقه',
#                 'suc_url': self.success_url,
#                 }
#             return render(request, self.template, ctx)
#         form.save()
#         try:
#             if request.POST['check'] == 'on':
#                 ctx = {
#                         'form': SessionForm(
#                             initial={
#                                 'check': 'on'
#                                 }
#                             ),
#                         'suc_url': self.success_url,
#                         'type':'محفظ'
#                         }
#                 return render(request, self.template, ctx)
#         except:
#             pass
#         return redirect(self.success_url)
    

# class SessionUpdate(View):
#     model = Session
#     success_url = reverse_lazy('session')
#     template = 'add_update_form.html'

#     def get(self, request, pk, next=''):
#         success_url = check_suc_url(next, self.success_url)
#         session = get_object_or_404(self.model, pk=pk)
#         form = SessionForm(instance=session)
#         ctx = {
#             'form': form,
#             'type': 'حلقه',
#             'suc_url': success_url,
#             'update': True
#             }
#         return render(request, self.template, ctx)

#     def post(self, request, pk, next=''):
#         success_url = check_suc_url(next, self.success_url)
#         session = get_object_or_404(self.model, pk=pk)
#         form = SessionForm(request.POST, instance=session)
#         if not form.is_valid():
#             ctx = {
#                 'form': form,
#                 'type': 'حلقه',
#                 'suc_url': success_url,
#                 'update': True
#                 }
#             return render(request, self.template, ctx)
#         form.save()
#         return redirect(self.success_url)

# class SessionDelete(View):
#     model = Session
#     success_url = reverse_lazy('session')
#     template = 'make_confirm_delete.html'
#     def get(self, request, pk, next=''):
#         success_url = check_suc_url(next, self.success_url)
#         session = get_object_or_404(self.model, pk=pk)
#         form = SessionForm(instance=session)
#         ctx = {'model': session, 'type': 'حلقه', 'suc_url':success_url }
#         return render(request, self.template, ctx)

#     def post(self, request, pk, next=''):
#         success_url = check_suc_url(next, self.success_url)
#         make = get_object_or_404(self.model, pk=pk)
#         make.delete()
#         return redirect(success_url)
