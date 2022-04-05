from django.forms import ModelForm
from .models import Manager, Room, Teacher, Session, Student, StudentSessions
from django import forms

# Create the form class.
class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'
        labels = {
            'name': ('الاسم'),
            'n_id': ('الرقم القومى'),
            'address': ('العنوان'),
            'phone': ('رقم التليفون'),
            'home_number': ('التليفون الارضي'),
            'salary': 'الراتب'
        }

        
class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        labels = {
            'name': ('الاسم'),
            'n_id': ('الرقم القومى'),
            'address': ('العنوان'),
            'phone': ('رقم التليفون'),
            'home_number': ('التليفون الارضي')
        }
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        labels = {
            'name': ('اسم الغرفة'),
            }

class SessionForm(ModelForm):
    time = forms.TimeField(initial='00:00')
    class Meta:
        model = Session
        fields = '__all__'
        labels = {
            'day': ('يوم'),
            'teacher':('اسم المحفظ'),
            'time':('الميعاد'),
            'name':('اسم الغرفة'),
        }
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': ('الاسم'),
            'n_id': ('الرقم القومى'),
            'address': ('العنوان'),
            'phone': ('رقم التليفون'),
            'home_number': ('التليفون الارضي')
        }
class StudentSessionsForm(ModelForm):
    class Meta:
        model = StudentSessions
        fields = '__all__'
        labels = {
            '_student': ('الطالب'),
            '_session': ('الحلقة')
        }
# class ManagerForm(ModelForm):
#     class Meta:
#         model = Manager
#         fields = '__all__'
#         labels = {
#             'name': ('الاسم'),
#             'n_id': ('الرقم القومى'),
#             'address': ('العنوان'),
#             'phone': ('رقم التليفون'),
#             'home_number': ('التليفون الارضي')
#         }
