
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import*

# Create your views here.
def home(request):
    jobs= JobPost.objects.all()
    
    return render(request,'home.html',{"jobs":jobs})
def login(request):
    return render(request,'login.html')
def login_req(request):
    return render(request,'login.html')
def sign_up(request):
    return render(request,'signup.html')
def signup_handel(request):
    if request.method == 'POST':
        username = request.POST['username']
        email =  request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            user = User.objects.create_user(username,email,password)
            user.save()
def job_application(request):
    
    return render(request,'job_application.html')
def job_details(request,j_id):
    job = JobPost.objects.get(id=j_id)

    return render(request,'job_details.html',{"job":job})


