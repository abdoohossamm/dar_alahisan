import re
from app.models import Session, StudentSessions
from django import template


register = template.Library()


@register.filter(name= 'get_sessions_day')
def get_sessions_day(day, teacher=1):
    result = list()
    sessions =  Session.objects.filter(day=day, teacher=teacher)
    for session in sessions:
        result.append(session)
    if len(result) > 0:
        return result
    return ['لا يوجد']


@register.filter(name= 'format_session')
def format_session(session) -> str :
    if isinstance(session, str):
            return session
    return f'غرفة {session.name} الساعة {session.time}'



@register.filter(name= 'get_students_session')
def get_students_session(session):
    if isinstance(session, str):
        return 0
    return StudentSessions.objects.filter(session=session).count()



@register.filter(name= 'students_number')
def students_number(session):
    return StudentSessions.objects.filter(session= session).count()

@register.filter(name='range') 
def times(number:int):
    try:
        num = int(number)
    except:
        return None
    return range(1, number+1)

@register.filter(name= 'get_sessions_day_student')
def get_sessions_day_student(day, student=1):
    result = list()
    sessions =  StudentSessions.objects.filter(session__day=day, student=student).select_related('session__teacher', 'session__name')
    for session in sessions:
        result.append(session)
    if len(result) > 0:
        return result
    return ['لا يوجد']