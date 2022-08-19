from django.urls import path,include
from . import views

app_name = 'reports'

urlpatterns = [
    
    path('session_report/', views.SessionReportView.as_view(), name='session_report'),
    path('session_report/<int:session_pk>/<int:month>/<int:year>/', views.StudentReportDetailView.as_view(), name='session_report'),
    path('session_report/<int:session_pk>/', views.StudentReportDetailView.as_view(), name='session_report'),
    path('student_attend/<int:session_report>/<path:next>/', views.StudentAttendSessionView.as_view(), name='student_session_attend'),
    path('student_attend/<int:session_report>/', views.StudentAttendSessionView.as_view(), name='student_session_attend'),
    path('student_report/<int:student>/', views.StudentReportView.as_view(), name='student_report'),
    path('student_report/<int:student>/<path:next>/', views.StudentReportView.as_view(), name='student_report'),
    # SessionReporter CRUD    
    path('session_report/create/', views.SessionReporterCreate.as_view(), name='session_report_create'),
    path('session_report/create/<int:session>/', views.SessionReporterCreate.as_view(), name='session_report_create'),
    path('session_report/create/<int:session>/<path:next>/', views.SessionReporterCreate.as_view(), name='session_report_create'),

    path('session_report/<int:pk>/update/next=<path:next>/', views.SessionReporterUpdate.as_view(), name='session_report_update'),
    path('session_report/<int:pk>/update/', views.SessionReporterUpdate.as_view(), name='session_report_update'),
    
    path('session_report/<int:pk>/delete/next=<path:next>/', views.SessionReporterDelete.as_view(), name='session_report_delete'),
    path('session_report/<int:pk>/delete/', views.SessionReporterDelete.as_view(), name='session_report_delete'),
    # Student Reporter CRUD    
    path('student_report/create/', views.StudentReportCreateView.as_view(), name='student_report_create'),
    path('student_report/create/<int:pk>/', views.StudentReportCreateView.as_view(), name='student_report_create'),
    path('student_report/create/<int:pk>/<path:next>/', views.StudentReportCreateView.as_view(), name='student_report_create'),
    path('student_report/create/<path:next>/', views.StudentReportCreateView.as_view(), name='student_report_create'),

    path('student_report_update/<int:pk>/update/next=<path:next>/', views.StudentReportUpdateView.as_view(), name='student_report_update'),
    path('student_report_update/<int:pk>/update/', views.StudentReportUpdateView.as_view(), name='student_report_update'),
    
    path('student_report_delete/<int:pk>/delete/next=<path:next>/', views.StudentReportDeleteView.as_view(), name='student_report_delete'),
    path('student_report_delete/<int:pk>/delete/', views.StudentReportDeleteView.as_view(), name='student_report_delete'),
    path('student_attend/<int:session_report>/<int:pk>/<int:change>/<path:next>/', views.change_student_attend_status, name="student_attend_status")
]