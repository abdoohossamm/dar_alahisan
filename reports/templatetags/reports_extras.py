import re
from app.models import Session, StudentSessions
from django import template


register = template.Library()


@register.filter(name= 'day_in_arabic')
def day_in_arabic(day):
    days = {
        'Saturday':'السبت',
        'Sunday':'الاحد',
        'Monday':'الاثنين',
        'Tuesday':'الثلاثاء',
        'Wednesday':'الاربعاء',
        'Thursday':'الخميس',
        'Friday':'الجمعة',
    }
    for k, v in days.items():
        if k in day:
            result = str(day).replace(k, v)
            return result
    return ''