from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('home', views.home, name='home'),
  path('login',views.login,name='login_req'),
  path('login_req_process',views.login_req,name="login"),
  path('sign_up',views.sign_up,name='sign_req'),
  path('signup_handel',views.signup_handel,name='sign_req'),

]



