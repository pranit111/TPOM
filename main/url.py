from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name='home'),
  path('login',views.login_req,name='login_req'),
  path('logout',views.user_logout,name='logout'),
  path('login_view',views.login_view,name="login_view"),
  path('sign_up',views.sign_up,name='sign_req'),
  path('signup_handel',views.signup_handel,name='signup'),
  path('job_application/<int:a_id>',views.job_application,name='job_application'),
  path('job_details/<int:j_id>',views.job_details,name='job_details'),
  path('job_application_save/<int:job_post_id>',views.job_application_save,name='job_application_save'),
  path('profile', views.student_profile, name='student_profile'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('trainning',views.training,name="training"),
  path('overview/', views.overview, name='overview'),
  path('applied_jobs/', views.applied_jobs, name='applied_jobs'),
  path('training_sessions/', views.training_sessions, name='training_sessions'),
  path('job_alerts/', views.job_alerts, name='job_alerts'),
  path('edit_profile/', views.edit_profile, name='edit_profile'),
  path('help_support/', views.help_support, name='help_support'),
  path('rejection_insights/', views.rejection_insights, name='rejection_insights'),
  path('training_home/', views.training_home, name='training_home'),
 
  path('training_programs/<int:id>',  views.training_detail, name='training_programs'),
      # Training programs page
  path('search_training_programs/', views.search_training_programs, name='search_training_programs'),   
  path('enroll/<int:program_id>/', views.enroll_program, name='enroll_program'),
]



