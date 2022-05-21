from django.urls import path,include
from . import views
from .main_views import manager_views as mv
from .main_views import room_views as rv
from .main_views import session_views as sv
from .main_views import teacher_views as tv
from .main_views import student_views as stv
from .main_views import student_session_views as ssv
from django.contrib.auth import views as vi

urlpatterns = [
    # main views
    path('', views.MainView.as_view(), name='index'),
    path('days/', views.DaysView.as_view(), name='days'),
    path('manager/', mv.ManagerDetailsView.as_view(), name='manager'),
    path('room/', rv.RoomDetailsView.as_view(), name='room'),
    path('student/', stv.StudentView.as_view(), name='student'),
    path('student/<int:pk>/', stv.StudentDetailsView.as_view(), name='student_details'),
    path('session/', sv.SessionView.as_view(), name='session'),
    path('teacher/', tv.TeachersView.as_view(), name='teacher'),
    path('teacher/<int:pk>/', tv.TeacherDetailsView.as_view(), name='teacher_details'),
    path('stu_session_<int:session>/create/next=<path:next>/', ssv.StudentSessionCreate.as_view(), name='student_session_create'),
    path('stu_session_<int:student>/create/next=<path:next>/', ssv.StudentSessionCreate.as_view(), name='student_session_create'),
    path('stu_session/<int:student>/<int:session>/create/', ssv.StudentSessionCreate.as_view(), name='student_session_create'),
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
    # room CRUD
    path('room/create/', rv.RoomCreate.as_view(), name='room_create'),
    path('room/<int:pk>/update/', rv.RoomUpdate.as_view(), name='room_update'),
    path('room/<int:pk>/update/?next=<path:next>/', rv.RoomUpdate.as_view(), name='room_update'),
    path('room/<int:pk>/delete/', rv.RoomDelete.as_view(), name='room_delete'),
    path('room/<int:pk>/delete/?next=<path:next>/', rv.RoomDelete.as_view(), name='room_delete'),    
    # student CRUD
    path('student/create/', stv.StudentCreate.as_view(), name='student_create'),
    path('student/<int:pk>/update/', stv.StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/update/?next=<path:next>/', stv.StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', stv.StudentDelete.as_view(), name='student_delete'),
    path('student/<int:pk>/delete/?next=<path:next>/', stv.StudentDelete.as_view(), name='student_delete'),
    # session CRUD
    path('session/create/', sv.SessionCreate.as_view(), name='session_create'),
    path('session/create/<int:day>/<int:teacher>/next=<path:next>/', sv.SessionCreate.as_view(), name='session_create'),
    path('session/create/<int:day>/<int:teacher>/', sv.SessionCreate.as_view(), name='session_create'),
    path('session/<int:pk>/update/next=<path:next>/', sv.SessionUpdate.as_view(), name='session_update'),
    path('session/<int:pk>/update/', sv.SessionUpdate.as_view(), name='session_update'),
    path('session/<int:pk>/delete/next=<path:next>/', sv.SessionDelete.as_view(), name='session_delete'),
    path('session/<int:pk>/delete/', sv.SessionDelete.as_view(), name='session_delete'),
    # teacher CRUD
    path('teacher/create/', tv.TeacherCreate.as_view(), name='teacher_create'),
    path('teacher/<int:pk>/update/', tv.TeacherUpdate.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/update/?next=<path:next>/', tv.TeacherUpdate.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/delete/', tv.TeacherDelete.as_view(), name='teacher_delete'),
    path('teacher/<int:pk>/delete/?next=<path:next>/', tv.TeacherDelete.as_view(), name='teacher_delete'),
    # Student Session CRUD
    path('student_session/<int:pk>/delete/next=<path:next>', ssv.StudentSessionDelete.as_view(), name='student_session_delete'),
    path('student_session/<int:pk>/update/next=<path:next>', ssv.StudentSessionUpdate.as_view(), name='student_session_update'),
    path('student_session/<int:student>/<int:day>/next=<path:next>', ssv.StudentSessionsCreateByDay.as_view(), name='student_session_create'),
    
]