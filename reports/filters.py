from psycopg2 import Date
import django_filters #type: ignore
from .models import SessionReporter,StudentReporter,AttendanceChoice
from app.models import Session, Teacher
from django import forms
from django_filters import DateFilter,ChoiceFilter, CharFilter, ModelChoiceFilter # type: ignore
from django.conf import settings
from .forms import DateInput


class SessionReporterFilter(django_filters.FilterSet):
    session = ModelChoiceFilter(label="الحلقة",
                            queryset=Session.objects.all().select_related('teacher', 'name','day').order_by('teacher__name'))
    teacher = ModelChoiceFilter(label="المحفظ",
                            queryset=Teacher.objects.all().order_by('name'), field_name="session__teacher")
    session_date = DateFilter(label="تاريخ الحلقة", 
                            widget=DateInput() ,field_name='session_date')
    
    report = CharFilter(label="تقرير الحفظ", 
                            field_name='report', lookup_expr='icontains')
    
    review_report = CharFilter(label="تقرير المراجعة",
                            field_name='review_report', lookup_expr='icontains')
    
    start_date = DateFilter(widget=DateInput(),
                            label= 'من تاريخ',field_name='session_date', lookup_expr='gte')
    
    end_date = DateFilter(widget=DateInput(), 
                            label= 'الى تاريخ',field_name='session_date', lookup_expr='lte')


    def __init__(self, *args, **kwargs):
        super(SessionReporterFilter, self).__init__(*args, **kwargs)
        self.filters['session'].label="الحلقة"
        self.filters['session_date'].label="تاريخ الحلقة"
        self.filters['report'].label="تقرير الحفظ"
        self.filters['review_report'].label="تقرير المراجعة"
        
class StudentReporterFilter(django_filters.FilterSet):
    session = ModelChoiceFilter(label="الحلقة",
                            queryset=SessionReporter.objects.all(), field_name="session_report")
    attend = ChoiceFilter(label="الحضور", 
                            field_name='attend', lookup_expr='icontains', choices= AttendanceChoice)
    
    money = CharFilter(label="الدفع",
                            field_name='money', lookup_expr='icontains')
    session_date = DateFilter(label="تاريخ الحلقة", 
                            widget=DateInput() ,field_name='session_report__session_date')
    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial')# type: ignore
        try:
            student = initial['student']# type: ignore
        except:
            student=False
        super(StudentReporterFilter, self).__init__(*args, **kwargs)
        if student:
            session = SessionReporter.objects.select_related('session', 'session__teacher', 'session__name', 'session__day').filter(student_session_report__student=student)
            self.filters['session'] = ModelChoiceFilter(label="الحلقة",
                            queryset=session, field_name="session_report")
        self.filters['session'].label="الحلقة"
        self.filters['attend'].label="الحضور"
        self.filters['money'].label="الدفع"
        self.filters['session_date'].label="التاريخ"