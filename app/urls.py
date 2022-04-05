from django.urls import path,include
from . import views
from .main_views import manager_views as mv
from .main_views import session_views as sv
from .main_views import teacher_views as tv
from .main_views import student_views as stv
from django.contrib.auth import views as vi

urlpatterns = [
    # main views
    path('', views.MainView.as_view(), name='index'),
    path('today/', views.TodayView.as_view(), name='today'),
    
    path('manager/', mv.ManagerDetailsView.as_view(), name='manager'),
    path('student/', stv.StudentView.as_view(), name='student'),
    path('student/<int:pk>/', stv.StudentDetailsView.as_view(), name='student_details'),
    path('session/', sv.SessionView.as_view(), name='session'),
    path('teacher/', tv.TeachersView.as_view(), name='teacher'),
    path('teacher/<int:pk>/', tv.TeacherDetailsView.as_view(), name='teacher_details'),
    path('stu_session_<int:session_pk>/create/', views.StudentSessionCreate.as_view(), name='student_session_create'),
    path('stu_session_<int:student_pk>/create/', views.StudentSessionCreate.as_view(), name='student_session_create'),
    path('stu_session/<int:student_pk>/<int:session_pk>/create/', views.StudentSessionCreate.as_view(), name='student_session_create'),
    # account views
    path('logout/', vi.LogoutView.as_view(), name='logout'),
    path('login/', vi.LoginView.as_view(template_name='login.html'), name='login'),
    path('change_password/', vi.PasswordChangeView.as_view(template_name='change_pass.html'), name='changepassword'),
    path('change_password/done/', vi.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name= 'password_change_done')
]

# CRUD URl
urlpatterns += [    
    # manager CRUD
    path('manager/create/', mv.ManagerCreate.as_view(), name='manager_create'),
    path('manager/<int:pk>/update/', mv.ManagerUpdate.as_view(), name='manager_update'),
    path('manager/<int:pk>/update/?next=<path:next>/', mv.ManagerUpdate.as_view(), name='manager_update'),
    path('manager/<int:pk>/delete/', mv.ManagerDelete.as_view(), name='manager_delete'),
    path('manager/<int:pk>/delete/?next=<path:next>/', mv.ManagerDelete.as_view(), name='manager_delete'),    
    # student CRUD
    path('student/create/', stv.StudentCreate.as_view(), name='student_create'),
    path('student/<int:pk>/update/', stv.StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/update/?next=<path:next>/', stv.StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', stv.StudentDelete.as_view(), name='student_delete'),
    path('student/<int:pk>/delete/?next=<path:next>/', stv.StudentDelete.as_view(), name='student_delete'),
    # session CRUD
    path('session/create/', sv.SessionCreate.as_view(), name='session_create'),
    path('session/<int:pk>/update/?next=<path:next>/', sv.SessionUpdate.as_view(), name='session_update'),
    path('session/<int:pk>/update/', sv.SessionUpdate.as_view(), name='session_update'),
    path('session/<int:pk>/delete/?next=<path:next>/', sv.SessionDelete.as_view(), name='session_delete'),
    path('session/<int:pk>/delete/', sv.SessionDelete.as_view(), name='session_delete'),
    # teacher CRUD
    path('teacher/create/', tv.TeacherCreate.as_view(), name='teacher_create'),
    path('teacher/<int:pk>/update/', tv.TeacherUpdate.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/update/?next=<path:next>/', tv.TeacherUpdate.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/delete/', tv.TeacherDelete.as_view(), name='teacher_delete'),
    path('teacher/<int:pk>/delete/?next=<path:next>/', tv.TeacherDelete.as_view(), name='teacher_delete'),
]