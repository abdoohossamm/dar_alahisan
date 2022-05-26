import re
from app.models import Session, Day, Manager,StudentSessions,Teacher
from django import template
register = template.Library()


@register.filter(name= 'session_today')
def session_today(day_id):
    session_today = Session.objects.filter(day=day_id).select_related('name', 'teacher').order_by('time')
    return session_today

@register.filter(name= 'session_count')
def session_count(day_id):
    return Session.objects.filter(day=day_id).count()

@register.filter(name= 'student_count')
def student_count(day_id):
    student_count = StudentSessions.objects.filter(session__day= day_id).count()
    return student_count

#old code
# @register.filter(name= 'teacher_count')
# def teacher_count(day_id):
#     session_today = Session.objects.filter(day=day_id).select_related('teacher')
#     teacher = Teacher.objects.all()
#     teachers=[]
#     for teach in teacher:
#         if session_today.filter(teacher=teach) and teach not in teachers: 
#             teachers.append(teach)
#     return len(teachers)

#new code
@register.filter(name= 'teacher_count')
def teacher_count(day_id):
    teachers_count = Session.objects.filter(day=day_id).values('teacher').distinct().count()
    return teachers_count
