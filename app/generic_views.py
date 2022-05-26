from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db import models
from django import forms
from .functions import check_suc_url
import time
'''
CRUD Views
'''

class CRUDCreate(View):
    template = 'add_update_form.html'
    success_url = ''
    type=""
    form = forms.ModelForm
    initial = {}
    def get(self, request, next='', **initial):
        for k, v in initial.items():
            self.initial[k] = [v]
        self.success_url = check_suc_url(next, self.success_url)
        ctx = {
            'form': self.form(initial=self.initial),
            'suc_url': self.success_url,
            'type': self.type
            }
        return render(request, self.template, ctx)


    def post(self, request,next='', **initial):
        form = self.form(request.POST)
        print('Post request:',request.POST)
        self.success_url = check_suc_url(next, self.success_url)
        if not form.is_valid():
            ctx = {
                'form': form,
                'suc_url': self.success_url,
                'type':self.type
                }
            return render(request, self.template, ctx)
        form.save()
        try:
            if request.POST['add_another'] == 'on':
                merge = {"add_another": [True]}
                form = self.form(initial={**self.initial, **merge})
                ctx = {
                'form': form,
                'suc_url': self.success_url,
                'type':self.type
                }
                return render(request, self.template, ctx)
        except:
            pass
        return redirect(self.success_url)
    
    
    
class CRUDUpdate(View):
    model = models.Model
    success_url = ''
    template = 'add_update_form.html'
    form = forms.ModelForm
    type = ''
    def get(self, request, pk, next=''):
        instance_data = get_object_or_404(self.model, pk=pk)
        form = self.form(instance=instance_data)
        success_url = check_suc_url(next, self.success_url)
        ctx = {
            'form': form,
            'type': self.type,
            'suc_url': success_url,
            'update': True
            }        
        return render(request, self.template, ctx)

    def post(self, request, pk, next=''):
        instance_data = get_object_or_404(self.model, pk=pk)
        form = self.form(request.POST, instance=instance_data)
        success_url = check_suc_url(next, self.success_url)
        ctx = {
                'form': form,
                'type': self.type,
                'suc_url': success_url,
                'update': True
                }
        if not form.is_valid():
            return render(request, self.template, ctx)
        form.save()
        
        return redirect(success_url)


class CRUDDelete(View):
    model = models.Model
    success_url = ''
    template = 'make_confirm_delete.html'
    type = ''
    def get(self, request, pk, next=''):
        success_url = check_suc_url(next, self.success_url)
        instance_data = get_object_or_404(self.model, pk=pk)
        ctx = {
            'model': instance_data,
            'type': self.type,
            'suc_url':success_url 
            }
        
        return render(request, self.template, ctx)

    def post(self, request, pk, next=''):
        success_url = check_suc_url(next, self.success_url)
        make = get_object_or_404(self.model, pk=pk)
        from django.db.models import ProtectedError
        try:
            make.delete()
        except ProtectedError as e:
            error = f"""لا يمكن حذف {self.type} {make} لانة مرتبط ببيانات اخرى
            \n يجرى التأكد من حذف البيانات والمحاولة بعد ذلك\n
            اذا كان محفظ تأكد من حذف كل الحلقات الخاصة بة
            """
            ctx = {
            'error': error,
            'suc_url':success_url 
            }
            return render(request, 'errors.html', ctx)
        return redirect(success_url)


class StudentToSession(View):
    template = 'session/student_session.html'
    success_url = ''
    form = forms.ModelForm
    student = ''
