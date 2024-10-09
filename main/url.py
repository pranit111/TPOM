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
  path('job_application',views.job_application,name='job_application'),
  path('job_details/<int:j_id>',views.job_details,name='job_details'),
  path('profile', views.student_profile, name='student_profile'),

 
]



