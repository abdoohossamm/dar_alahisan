from django.contrib import admin
from reports.models import SessionReporter
# Register your models here.
class SessionReporterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("session",)}
    list_display = ('session', 'session_date', 'report', 'review_report')
admin.site.register(SessionReporter, SessionReporterAdmin)