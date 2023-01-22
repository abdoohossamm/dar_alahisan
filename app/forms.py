from django.forms import ModelForm
from .models import Manager, Room, Teacher, Session, Student, StudentSessions, Branch
from django import forms


class TimeInput(forms.TimeInput):
    input_type = 'time'

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
            'name': 'اسم الغرفة',
            'branch': 'الفرع',
            }


class BranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
        labels = {
            'name': 'اسم الفرع '
            }


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'
        labels = {
            'day': ('يوم'),
            'teacher':('اسم المحفظ'),
            'time':('الميعاد'),
            'name':('اسم الغرفة'),
        }
        widgets={'time':TimeInput()}
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
    session = forms.ModelChoiceField(queryset=Session.objects.all().select_related('teacher', 'name','day'))
    class Meta:
        model = StudentSessions
        fields = '__all__'
        labels = {
            'student': ('الطالب'),
            'session': ('الحلقة')
        }
    def __init__(self, *args, **kwargs):
        day = kwargs.pop('day', '')
        teacher = kwargs.pop('teacher', '')
        super(StudentSessionsForm, self).__init__(*args,**kwargs)
        if day and teacher:
            self.fields['session'].queryset = Session.objects.filter(day= day, teacher= teacher)  # type: ignore
        elif day:
            self.fields['session'].queryset = Session.objects.filter(day= day)  # type: ignore
        elif teacher:
            self.fields['session'].queryset = Session.objects.filter(teacher= teacher)  # type: ignore
