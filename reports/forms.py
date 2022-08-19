from django import forms
from reports.models import SessionReporter ,StudentReporter
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from app.functions import day_in_arabic
from app.models import Session,Student, StudentSessions
from django.db import IntegrityError


class DateInput(forms.DateInput):
    input_type = 'date'
    format=('%Y-%d-%m')

# Create your models here.
def day_of_date(date: datetime.date):
    days = {
        'Saturday':['السبت',1],
        'Sunday':['الاحد',2],
        'Monday':['الاثنين',3],
        'Tuesday':['الثلاثاء',4],
        'Wednesday':['الاربعاء',5],
        'Thursday':['الخميس',6],
        'Friday':['الجمعة',7],
    }
    day = str(date.strftime('%A'))
    day_name = days[day][0]
    return day_name

# class SessionReportForm(forms.Form):
class SessionReporterForm(forms.ModelForm):
    session = forms.ModelChoiceField(queryset=Session.objects.all().select_related('teacher', 'name','day'))
    class Meta:
        model = SessionReporter
        exclude = ['slug']
        widgets = {
            'session_date': DateInput(),
        }
        labels = {
            'session': ('الحلقة'),
            'session_date': ('تاريخ الحلقة'),
            'report': ('تقرير الحفظ'),
            'review_report': ('تقرير المراجعة'),
        }

    def clean(self):
        cleaned_data = self.cleaned_data # individual field's clean methods have already been called
        session_date = cleaned_data.get("session_date")
        print('session date', session_date)
        session = cleaned_data.get("session")
        if SessionReporter.objects.filter(session=session, session_date=session_date).exists():
            raise forms.ValidationError(_(f"يوجد تقرير لنفس الحلقة بنفس التاريخ, لا يمكن اضافة واحدة اخرى ويمكن التعديل عليها")) # type: ignore
        day_date = day_of_date(session_date)  # type: ignore
        if day_date != str(session.day):    # type: ignore
            self.add_error('session_date', f"التاريخ '{session_date}' غير مطابق ليوم الحلقة '{session.day}'") # type: ignore
            raise forms.ValidationError(_(f"التاريخ '{session_date}' غير مطابق ليوم الحلقة '{session.day}'")) # type: ignore

        else:
            return cleaned_data

class StudentReporterCreateForm(forms.ModelForm):
    class Meta:
        model = StudentReporter
        fields = '__all__'
        # exclude = ['session_report']
        labels = {
            'student': ('الطالب'),
            'session_report': ('الحلقة'),
            'attend': ('الحضور'),
            'money': ('الدقع'),
        }
    def __init__(self, *args, **kwargs):
        # inst = kwargs.pop('instance', '')
        init = kwargs.pop('initial', '')
        # print(init['session_report'])
        try:
            session_report = init['session_report']# type: ignore
        except:
            session_report=False
        super(StudentReporterCreateForm, self).__init__(*args,**kwargs)
        if session_report:
            session_rep = session_report.pk # type: ignore
            # session_rep = StudentReporter.objects.get(pk=pk).session_report.pk
            session = SessionReporter.objects.select_related('session', 'session__teacher', 'session__name', 'session__day').get(pk=session_rep).session.pk
            session_report = SessionReporter.objects.filter(pk=session_rep).select_related('session', 'session__teacher', 'session__day', 'session__name')
            students = Student.objects.filter(student_session__session=session).select_related('teacher')
            self.fields['student'] = forms.ModelChoiceField(queryset= students)
            self.fields['session_report'] = forms.ModelChoiceField(queryset= session_report)
            self.fields['session_report'].initial = session_report.get(pk=session_rep)

class StudentReporterUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentReporter
        fields = '__all__'
        exclude = ['session_report', 'student']
        labels = {
            'student': ('الطالب'),
            'session_report': ('الحلقة'),
            'attend': ('الحضور'),
            'money': ('الدقع'),
        }

class StudentAttendForm(forms.ModelForm):
    class Meta:
        model = StudentReporter
        fields =('attend',)
        labels = {
            'attend': ('حالة الحضور')
        }