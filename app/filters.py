from psycopg2 import Date
import django_filters #type: ignore
from app.models import Session, Teacher, Branch
from django import forms
from django_filters import DateFilter, CharFilter, ModelChoiceFilter # type: ignore
from django.conf import settings
from .forms import TimeInput

class SessionFilter(django_filters.FilterSet):
    time = CharFilter(label='الميعاد', field_name='time', widget=TimeInput())
    branch = django_filters.ModelChoiceFilter(queryset=Branch.objects.all(), field_name="name__branch")

    class Meta:
        model = Session
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SessionFilter, self).__init__(*args, **kwargs)
        self.filters['day'].label="يوم"
        self.filters['teacher'].label="اسم المحفظ"
        self.filters['time'].label="الميعاد"
        self.filters['name'].label="الغرفة"
        self.filters['branch'].label = "الفرع"