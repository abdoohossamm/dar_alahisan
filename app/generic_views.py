from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db import models
from django import forms


def check_suc_url(next, success_url):
    if next == '':
        return success_url
    else:
        return next


'''
CRUD Views
'''

class CRUDCreate(View):
    template = 'add_update_form.html'
    success_url = ''
    type=""
    form = forms.ModelForm
    
    def get(self, request):
        ctx = {
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
        try:
            if request.POST['add_another'] == 'on':
                form = self.form(initial={"add_another": True})
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
    form = forms.ModelForm
    template = 'make_confirm_delete.html'
    type = ''
    def get(self, request, pk, next=''):
        success_url = check_suc_url(next, self.success_url)
        instance_data = get_object_or_404(self.model, pk=pk)
        form = self.form(instance=instance_data)
        ctx = {
            'model': instance_data,
            'type': self.type,
            'suc_url':success_url 
            }
        
        return render(request, self.template, ctx)

    def post(self, request, pk, next=''):
        success_url = check_suc_url(next, self.success_url)
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        
        return redirect(success_url)
class StudentToSession(View):
    template = 'session/student_session.html'
    success_url = ''
    form = forms.ModelForm
    student = ''