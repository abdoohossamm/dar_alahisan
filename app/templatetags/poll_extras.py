import re
from app.models import Session, StudentSessions
from django import template


register = template.Library()

@register.filter(name= 'get_sessions_day')
def get_sessions_day(day, teacher=1):
    result = list()
    for session in Session.objects.filter(day=day):
        if session.teacher.id == teacher:
            result.append(session)
    if len(result) > 0:
        return result
    return ['لا يوجد']



@register.filter(name= 'format_session')
def format_session(session):
    if isinstance(session, str):
            return session
    return f'غرفة {session.name} الساعة {session.time}'



@register.filter(name= 'get_students_session')
def get_students_session(session):
    if isinstance(session, str):
        return 0
    counter = 0
    for student_session in StudentSessions.objects.all():
        if str(student_session.session) == str(session):
            counter +=1
    return counter



@register.filter(name= 'students_number')
def students_number(session):
    return StudentSessions.objects.filter(session= session).count()
