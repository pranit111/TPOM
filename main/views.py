
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import logging
from .models import*
from .forms import *
# Create your views here.
@login_required
def home(request):
    current_user=request.user
    
    jobs= JobPost.objects.all()
    return render(request,'home.html',{"jobs":jobs,"user":current_user})
@login_required
def user_logout(request):
    logout(request)
    return redirect('login_req') 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, 'Login successful!')
            return redirect('/')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
def login_req(request):
    return render(request,'login.html')
def sign_up(request):
    skills=Skill.objects.all()
    return render(request,'signup.html',{'skills': skills})
def signup_handel(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        # Create and save the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
    
            return redirect('login')  # Redirect to login or any other page
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')

            # Create the associated student profil

            messages.success(request, 'Your account has been created successfully!')
            return redirect('login_req')  # Redirect to login or any other page
        else:
            messages.error(request, 'Please correct the errors below.')
    return render(request, 'signup.html')
def job_application(request):
    
    return render(request,'job_application.html')
def job_details(request,j_id):
    job = JobPost.objects.get(id=j_id)

    return render(request,'job_details.html',{"job":job})


@login_required
def student_profile(request):
    # Try to retrieve the student profile associated with the logged-in user
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None

    if request.method == 'POST':
        # If student exists, populate the form with instance, otherwise create new
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            # Save the form data to the database
            student = form.save(commit=False)
            student.user = request.user  # Associate the logged-in user with the student profile
            student.save()
            form.save_m2m()  # Save the many-to-many data for skills field
            return redirect('student_profile')  # Redirect to the profile view after saving
    else:
        # If student does not exist, create an empty form, otherwise populate it
        form = StudentForm(instance=student)

    # If student exists, render the profile page, otherwise render profile creation
    if student:
        return render(request, 'profile.html', {'form': form, 'student': student})
    else:
        print("usen not found")
        return render(request, 'profile_create.html', {'form': form})
