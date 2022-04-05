from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ..models import Teacher, Session, Day, StudentSessions
from ..forms import TeacherForm
from ..generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
'''
Teacher views
'''    
class TeachersView(LoginRequiredMixin, View):
    template = 'teacher/teacher.html'
    def get(self, request):
        teacher = Teacher.objects.all()
        ctx = {'teachers': teacher}
        return render(request, self.template, ctx)


class TeacherDetailsView(LoginRequiredMixin, View):
    template = 'teacher/teacher_details.html'
    model = Teacher
    def get(self, request, pk):
        teacher = get_object_or_404(self.model, pk=pk)
        session_ = Session.objects.filter(teacher=pk)
        days = Day.objects.all()
        success_url = reverse_lazy('teacher_details', kwargs={'pk':teacher.pk})
        ctx = {
            'teacher': teacher,
            'session': session_,
            'days': days,
            'suc_url': success_url
            }
        return render(request, self.template, ctx)



'''
CRUD Views
'''
class TeacherCreate(LoginRequiredMixin, CRUDCreate):
    template = 'add_update_form.html'
    success_url = reverse_lazy('teacher')
    type="محفظ"
    form = TeacherForm
    
    
class TeacherUpdate(LoginRequiredMixin, CRUDUpdate):
    model = Teacher
    success_url = reverse_lazy('teacher')
    template = 'add_update_form.html'
    form = TeacherForm
    type="محفظ"
    
    
class TeacherDelete(LoginRequiredMixin, CRUDDelete):
    model = Teacher
    success_url = reverse_lazy('teacher')
    form = TeacherForm
    template = 'make_confirm_delete.html'
    type = 'محفظ'



# class TeacherCreate(LoginRequiredMixin, View):
#     template = 'add_update_form.html'
#     success_url = reverse_lazy('teacher')
    
    
#     def get(self, request):
#         form = TeacherForm()
#         ctx = {
#             'form': form,
#             'suc_url': self.success_url,
#             'type':'محفظ'
#             }
#         return render(request, self.template, ctx)


#     def post(self, request):
#         form = TeacherForm(request.POST)

#         print(request.POST)
#         if not form.is_valid():
#             ctx = {
#                 'form': form,
#                 'suc_url': self.success_url,
#                 'type':'محفظ'
#                 }
#             return render(request, self.template, ctx)
#         form.save()
#         try:
#             if request.POST['add_another'] == 'on':
#                 form = TeacherForm(initial={"add_another": True})
#                 ctx = {
#                 'form': form,
#                 'suc_url': self.success_url,
#                 'type':'محفظ'
#                 }
#                 return render(request, self.template, ctx)
#         except:
#             pass
#         return redirect(self.success_url)
    
    
    
# class TeacherUpdate(LoginRequiredMixin, View):
#     model = Teacher
#     success_url = reverse_lazy('teacher')
#     template = 'add_update_form.html'

#     def get(self, request, pk, next=''):
#         teacher = get_object_or_404(self.model, pk=pk)
#         form = TeacherForm(instance=teacher)
#         success_url = check_suc_url(next, self.success_url)
#         ctx = {
#             'form': form,
#             'type': 'محفظ',
#             'suc_url': success_url,
#             'update': True
#             }        
#         return render(request, self.template, ctx)

#     def post(self, request, pk, next=''):
#         teacher = get_object_or_404(self.model, pk=pk)
#         form = TeacherForm(request.POST, instance=teacher)
#         success_url = check_suc_url(next, self.success_url)
#         ctx = {
#                 'form': form,
#                 'type': 'محفظ',
#                 'suc_url': success_url,
#                 'update': True
#                 }
#         if not form.is_valid():
#             return render(request, self.template, ctx)
#         form.save()
        
#         return redirect(success_url)
    
# class TeacherDelete(LoginRequiredMixin, View):
#     model = Teacher
#     success_url = reverse_lazy('teacher')
#     template = 'make_confirm_delete.html'

#     def get(self, request, pk, next=''):
#         success_url = check_suc_url(next, self.success_url)
#         teacher = get_object_or_404(self.model, pk=pk)
#         form = TeacherForm(instance=teacher)
#         ctx = {
#             'model': teacher,
#             'type': 'محفظ',
#             'suc_url':success_url 
#             }
        
#         return render(request, self.template, ctx)

#     def post(self, request, pk, next=''):
#         success_url = check_suc_url(next, self.success_url)
#         make = get_object_or_404(self.model, pk=pk)
#         make.delete()
        
#         return redirect(success_url)
