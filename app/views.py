from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from .models import Day,Room, Teacher, Session, StudentSessions, Student
from .forms import TeacherForm,StudentSessionsForm
from .functions import day_in_arabic
from .generic_views import CRUDCreate,CRUDUpdate, CRUDDelete
from .functions import check_suc_url




# class StudentSessionCreate(View):
#     template = 'add_update_form.html'
#     success_url = reverse_lazy('session')
#     type='طالب بالنسبة لحلقة'
#     form = StudentSessionsForm
#     student = ''
#     session = ''
#     initial = {
#             'student': student,
#             'session': session
#             }
    
#     def get(self, request, student=None, session=None, next=''):
#         self.initial['student'] = student
#         self.initial['session'] = session
#         self.success_url = check_suc_url(next, self.success_url)
#         ctx = {
#             'form': self.form(initial=self.initial),
#             'suc_url': self.success_url,
#             'type': self.type
#             }
#         return render(request, self.template, ctx)


#     def post(self, request, student=None, session=None, next=''):
#         form = self.form(request.POST)

#         print(request.POST)
#         if not form.is_valid():
#             ctx = {
#                 'form': form,
#                 'suc_url': self.success_url,
#                 'type':self.type
#                 }
#             return render(request, self.template, ctx)
#         form.save()
#         return redirect(self.success_url)


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
    day_pk = day_in_arabic()[1]
    def get(self, request):
        ctx = {
            'day_name': self.day_name,
            'day_pk': self.day_pk,
        }
        return render(request, self.template,ctx)

def _404_not_found(request):
    return render(request, '404.html',)

def developer_details(request):
    return render(request, 'developer_detail.html')