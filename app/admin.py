from dataclasses import field
from django.contrib import admin
from .models import Manager,Teacher, Room, Day, Session, Student, StudentSessions
# Register your models here.
admin.site.site_header= "لوحة المسؤول"
admin.site.site_title= "لوحة المسؤول"
class SessionAdmin(admin.ModelAdmin):
    field = '__all__'
    labels = {
        'Day': ('يوم'),
        'teacher':('اسم المحفظ'),
        'time':('الميعاد'),
        'name':('اسم الغرفة'),
    }
    list_display = ("day", 'time', 'name', 'teacher',)
    list_display_links = ('name', 'teacher')
    list_filter = ('day','name', 'teacher')
admin.site.register(Manager)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Day)
admin.site.register(Session, SessionAdmin)
admin.site.register(Student)
admin.site.register(StudentSessions)
