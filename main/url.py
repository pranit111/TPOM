from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name='home'),
  path('login',views.login,name='login_req'),
  path('login_req_process',views.login_req,name="login"),
  path('sign_up',views.sign_up,name='sign_req'),
  path('signup_handel',views.signup_handel,name='sign_req'),
  path('job_application',views.job_application,name='job_application'),
  path('job_details/<int:j_id>',views.job_details,name='job_details'),

]



