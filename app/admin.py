from django.contrib import admin
from .models import Manager,Teacher, Room, Day, Session, Student, StudentSessions
# Register your models here.

admin.site.register(Manager)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Day)
admin.site.register(Session)
admin.site.register(Student)
admin.site.register(StudentSessions)
