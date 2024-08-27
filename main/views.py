
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
 
    return render(request,'home.html')
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


