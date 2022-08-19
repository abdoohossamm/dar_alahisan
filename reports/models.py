from django.db import models
import datetime
from app.models import Session, Student
from django.core.exceptions import ValidationError


class SessionReporter(models.Model):
    session = models.ForeignKey(Session, related_name='session_report', on_delete=models.PROTECT)
    slug = models.SlugField()
    session_date = models.DateField(default=datetime.date.today)
    report = models.TextField(max_length=125, null=True, blank=True)
    review_report = models.TextField(max_length=125, null=True, blank=True)
    class Meta:
        unique_together = ['session', 'session_date']
    def __str__(self):
        return (f'حلقة {self.session} بتاريخ {self.session_date}') # type: ignore

AttendanceChoice = [('حضور','حضور'), ('غياب','غياب'), ('لم يتم التحديد','لم يتم التحديد')]
class StudentReporter(models.Model):
    student = models.ForeignKey(Student, related_name='student_report', on_delete=models.CASCADE)
    session_report = models.ForeignKey(SessionReporter, related_name='student_session_report', on_delete=models.CASCADE)
    attend = models.CharField(max_length=15, default='لم يتم التحديد', choices=AttendanceChoice, null=True)
    money = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    class Meta:
        unique_together = ['student', 'session_report']
    def __str__(self):
        return (f'تقرير الطالب {self.student} بتاريخ {self.session_report.session_date}') # type: ignore