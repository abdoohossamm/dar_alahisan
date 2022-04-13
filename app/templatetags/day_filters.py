import re
from app.models import Session, Day, Manager,StudentSessions,Teacher
from django import template
register = template.Library()


@register.filter(name= 'session_today')
def session_today(day_id):
    session_today = Session.objects.filter(day=day_id).order_by('time')
    return session_today

@register.filter(name= 'session_count')
def session_count(day_id):
    session_today = Session.objects.filter(day=day_id).order_by('time')
    return session_today.count()

@register.filter(name= 'student_count')
def student_count(day_id):
    session = Session.objects.all().order_by('time')
    student_counter = 0
    for i in session.filter(day=day_id):
        student_count = StudentSessions.objects.filter(session= i).count()
        student_counter += student_count
    return student_counter

@register.filter(name= 'teacher_count')
def teacher_count(day_id):
    session_today = Session.objects.filter(day=day_id).order_by('time')
    teacher = Teacher.objects.all()
    teachers=[]
    for teach in teacher:
        for i in session_today:
            if session_today.filter(teacher=teach) and teach not in teachers: 
                teachers.append(teach)
    return len(teachers)