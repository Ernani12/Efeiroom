
from django.urls import path,include
from . import AdmViews, ProfessorViews, views
from .import AlunoViews
from .views import CreateVideo, DetailVideo, Formulario, UpdateVideo, DeleteVideo


urlpatterns = [
    
    #Aplicacoes Brain, Gmeet, Formularios
    path('', views.home, name="home"),
    path('login', views.loginPage, name="login"),
    path('GMeet/', views.GMeet, name="GMeet"),
    path('Brainstorming/', views.Brainstorming, name="Brainstorming"),
    path('Formulario/', views.Formulario, name="Formulario"),
    path('Compilador', views.Compilador, name="Compilador"),
    path('live', views.live, name="live"),

    path('back', views.home, name="back"),
    path('about', views.about, name="about"),
    path('teachers', views.about, name="teachers"),
    path('contact', views.about, name="contact"),
    path('graficos', views.graficos, name="graficos"),
    path('gr', views.graficosRandom, name="gr"),
    path('calendario', views.calendario, name="calendario"),

    # URLS para Administrador
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', AdmViews.admin_home, name="admin_home"),
    path('add_staff/', AdmViews.add_staff, name="add_staff"),
    path('add_staff_save/', AdmViews.add_staff_save, name="add_staff_save"),
    path('manage_staff/', AdmViews.manage_staff, name="manage_staff"),
    path('edit_staff/<staff_id>/', AdmViews.edit_staff, name="edit_staff"),
    path('edit_staff_save/', AdmViews.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', AdmViews.delete_staff, name="delete_staff"),
    path('add_course/', AdmViews.add_course, name="add_course"),
    path('add_course_save/', AdmViews.add_course_save, name="add_course_save"),
    path('manage_course/', AdmViews.manage_course, name="manage_course"),
    path('edit_course/<course_id>/', AdmViews.edit_course, name="edit_course"),
    path('edit_course_save/', AdmViews.edit_course_save, name="edit_course_save"),
    path('delete_course/<course_id>/', AdmViews.delete_course, name="delete_course"),
    path('manage_session/', AdmViews.manage_session, name="manage_session"),
    path('add_session/', AdmViews.add_session, name="add_session"),
    path('add_session_save/', AdmViews.add_session_save, name="add_session_save"),
    path('edit_session/<session_id>', AdmViews.edit_session, name="edit_session"),
    path('edit_session_save/', AdmViews.edit_session_save, name="edit_session_save"),
    path('delete_session/<session_id>/', AdmViews.delete_session, name="delete_session"),
    path('add_student/', AdmViews.add_student, name="add_student"),
    path('add_student_save/', AdmViews.add_student_save, name="add_student_save"),
    path('edit_student/<student_id>', AdmViews.edit_student, name="edit_student"),
    path('edit_student_save/', AdmViews.edit_student_save, name="edit_student_save"),
    path('manage_student/', AdmViews.manage_student, name="manage_student"),
    path('delete_student/<student_id>/', AdmViews.delete_student, name="delete_student"),
    path('add_subject/', AdmViews.add_subject, name="add_subject"),
    path('add_subject_save/', AdmViews.add_subject_save, name="add_subject_save"),
    path('manage_subject/', AdmViews.manage_subject, name="manage_subject"),
    path('edit_subject/<subject_id>/', AdmViews.edit_subject, name="edit_subject"),
    path('edit_subject_save/', AdmViews.edit_subject_save, name="edit_subject_save"),
    path('delete_subject/<subject_id>/', AdmViews.delete_subject, name="delete_subject"),
    path('check_email_exist/', AdmViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', AdmViews.check_username_exist, name="check_username_exist"),
    path('student_feedback_message/', AdmViews.student_feedback_message, name="student_feedback_message"),
    path('student_feedback_message_reply/', AdmViews.student_feedback_message_reply, name="student_feedback_message_reply"),
    path('staff_feedback_message/', AdmViews.staff_feedback_message, name="staff_feedback_message"),
    path('staff_feedback_message_reply/', AdmViews.staff_feedback_message_reply, name="staff_feedback_message_reply"),
    path('student_leave_view/', AdmViews.student_leave_view, name="student_leave_view"),
    path('student_leave_approve/<leave_id>/', AdmViews.student_leave_approve, name="student_leave_approve"),
    path('student_leave_reject/<leave_id>/', AdmViews.student_leave_reject, name="student_leave_reject"),
    path('staff_leave_view/', AdmViews.staff_leave_view, name="staff_leave_view"),
    path('staff_leave_approve/<leave_id>/', AdmViews.staff_leave_approve, name="staff_leave_approve"),
    path('staff_leave_reject/<leave_id>/', AdmViews.staff_leave_reject, name="staff_leave_reject"),
    path('admin_view_attendance/', AdmViews.admin_view_attendance, name="admin_view_attendance"),
    path('admin_get_attendance_dates/', AdmViews.admin_get_attendance_dates, name="admin_get_attendance_dates"),
    path('admin_get_attendance_student/', AdmViews.admin_get_attendance_student, name="admin_get_attendance_student"),
    path('admin_profile/', AdmViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', AdmViews.admin_profile_update, name="admin_profile_update"),
    


    # URLS for Staff (professor)
    path('staff_home/', ProfessorViews.staff_home, name="staff_home"),
    path('staff_take_attendance/', ProfessorViews.staff_take_attendance, name="staff_take_attendance"),
    path('get_students/', ProfessorViews.get_students, name="get_students"),
    path('save_attendance_data/', ProfessorViews.save_attendance_data, name="save_attendance_data"),
    path('staff_update_attendance/', ProfessorViews.staff_update_attendance, name="staff_update_attendance"),
    path('get_attendance_dates/', ProfessorViews.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student/', ProfessorViews.get_attendance_student, name="get_attendance_student"),
    path('update_attendance_data/', ProfessorViews.update_attendance_data, name="update_attendance_data"),
    path('staff_apply_leave/', ProfessorViews.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save/', ProfessorViews.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback/', ProfessorViews.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save/', ProfessorViews.staff_feedback_save, name="staff_feedback_save"),
    path('staff_profile/', ProfessorViews.staff_profile, name="staff_profile"),
    path('staff_profile_update/', ProfessorViews.staff_profile_update, name="staff_profile_update"),
    path('staff_add_result/', ProfessorViews.staff_add_result, name="staff_add_result"),
    path('staff_add_result_save/', ProfessorViews.staff_add_result_save, name="staff_add_result_save"),

    # URSL for Estudante
    path('student_home/', AlunoViews.student_home, name="student_home"),
    path('student_view_attendance/', AlunoViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', AlunoViews.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave/', AlunoViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save/', AlunoViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback/', AlunoViews.student_feedback, name="student_feedback"),
    path('student_feedback_save/', AlunoViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile/', AlunoViews.student_profile, name="student_profile"),
    path('student_profile_update/', AlunoViews.student_profile_update, name="student_profile_update"),
    path('student_view_result/', AlunoViews.student_view_result, name="student_view_result"),

    #URLS  Videos aulas salvas
    
    path('create/', CreateVideo.as_view(), name='video-create'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='video-delete'),


    #para Calendario
    path("calender/", views.CalendarViewNew.as_view(), name="calendar"),
    path("calenders/", views.CalendarView.as_view(), name="calendars"),
    path("event/new/", views.create_event, name="event_new"),
    path("event/edit/<int:pk>/", views.EventEdit.as_view(), name="event_edit"),
    path("event/<int:event_id>/details/", views.event_details, name="event-detail"),
    path(
        "add_eventmember/<int:event_id>", views.add_eventmember, name="add_eventmember"
    ),
    path(
        "event/<int:pk>/remove",
        views.EventMemberDeleteView.as_view(),
        name="remove_event",
    ),
    path("all-event-list/", views.AllEventsListView.as_view(), name="all_events"),
    path(
        "running-event-list/",
        views.RunningEventsListView.as_view(),
        name="running_events",
    ),


    #urls de arquivos e trabalhos
    path('file', views.Home.as_view(), name='file'),
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
 
    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

]
