
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
def job_application(request,a_id):
    job = JobPost.objects.get(id=a_id)
    form = ApplicationForm()

    return render(request,'job_application.html', {'form': form,"job_post":job})
def job_application_save(request, job_post_id):
    job = get_object_or_404(JobPost, id=job_post_id)  # Retrieve the job post
    print("www")
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        print(request.user.student)
        print("www")
        if form.is_valid():
            application = form.save(commit=False)  # Save form but don't commit
            application.student = request.user.student  # Assuming you have a Student model linked to the user
            application.job_post = job  # Assign the job post
            application.save()  # Now commit to save the instance
            return redirect('home')  # Redirect after successful save
        else:
            # If the form is not valid, print errors to the console
            print(form.errors)  # Optional: print errors for debugging
    else:
        form = ApplicationForm()

    return render(request, 'job_application.html', {'form': form, 'job_post': job})

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
def apply_job(request):
    if request.method == 'POST':
        # Create a form instance with the submitted data and files
        form = ApplicationForm(request.POST, request.FILES)
        
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user.student  # Associate the application with the logged-in student
            application.save()  # Save the application instance to the database
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('home')  # Redirect to a success page
    else:
        form = ApplicationForm()  # Create a new form instance for GET requests

    return render(request, 'job_application', {'form': form})
def dashboard(request):
    if request.user.is_authenticated:

        return render(request, 'dashboard.html')
def training(request):

    return render(request, 'training.html')
@login_required
def training_home(request):
    program=TrainingProgram.objects.all()
    print(program)
    return render(request, 'training_home.html',{'programs':program})
def overview(request):
    student=Student.objects.get(user=request.user)
    job_applications_count=Application.objects.filter(student=student).count()
    enrolled_programs_count = TrainingProgram.objects.filter(students=student).count()
    applications_count = Application.objects.filter(student=student,status='Shortlisted').count()
    # You can fetch necessary data here

 
    return render(request, 'overview.html',{'job_applications_count':job_applications_count,'training_sessions_count':enrolled_programs_count,'upcoming_interviews_count':applications_count})

def applied_jobs(request):
    student = Student.objects.get(user=request.user)
    
    # Fetch all applications for this student
    applications = Application.objects.filter(student=student)
    # Fetch applied jobs data
    return render(request, 'applied_jobs.html',{'applications':applications})

def training_sessions(request):
   
    user = request.user  # Assuming user is logged in

    # Get the Student instance associated with the current user
    student = get_object_or_404(Student, user=user)

    # Fetch all training programs that the student is enrolled in
    enrolled_programs = student.training_programs.all()  # This should return a queryset

    # Print enrolled programs for debugging purposes


    print(enrolled_programs)
    # Fetch training     sessions data
    return render(request, 'training_session.html',{"programs":enrolled_programs})
def rejection_insights(request):
    student = Student.objects.get(user=request.user)
    applications = Application.objects.filter(student=student,status="Rejected")
    # Fetch rejection insights data
    return render(request, 'rejection_insights.html',{'applications':applications})

def job_alerts(request):
    # Fetch job alerts data
    return render(request, 'job_alerts.html')

def edit_profile(request):
    # Fetch profile data
    return render(request, 'edit_profile.html')

def help_support(request):
    return render(request, 'help_support.html')
def training_programs(request):
    # Get filter criteria from GET request
    category = request.GET.get('category', '')
    level = request.GET.get('level', '')
    mode = request.GET.get('mode', '')
    sort_by = request.GET.get('sort', '')

    # Fetch all training programs
    training_programs = TrainingProgram.objects.all()

    # Apply filters based on category, level, and mode if available
    if category:
        training_programs = training_programs.filter(category=category)
    if level:
        training_programs = training_programs.filter(level=level)
    if mode:
        training_programs = training_programs.filter(mode=mode)

    # Apply sorting if applicable
    if sort_by == 'price-low':
        training_programs = training_programs.order_by('price')
    elif sort_by == 'price-high':
        training_programs = training_programs.order_by('-price')
    elif sort_by == 'duration':
        training_programs = training_programs.order_by('end_date')
    elif sort_by == 'popularity':
        training_programs = training_programs.order_by('-enrollment_count')  # Assuming popularity = enrollment count

    # Featured programs (example: first 3 programs or based on some logic)
    featured_programs = training_programs[:3]

    context = {
        'training_programs': training_programs,
        'featured_programs': featured_programs,
    }
    return render(request, 'training_programs.html', context)
def training_detail(request, id):
    # Retrieve the specific training program by ID
    program = get_object_or_404(TrainingProgram, id=id)

    context = {
        'program': program,
    }
    return render(request, 'training_detail.html', context)
def search_training_programs(request):
    query = request.GET.get('q', '')

    # Search training programs by title or description
    if query:
        training_programs = TrainingProgram.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        training_programs = TrainingProgram.objects.all()

    context = {
        'training_programs': training_programs,
        'query': query,
    }
    return render(request, 'search_training_programs.html', context)
def enroll_program(request, program_id):
    program = get_object_or_404(TrainingProgram, id=program_id)
    user = request.user  # Assuming user is logged in

    # Get the Student instance associated with the current user
    student = get_object_or_404(Student, user=user)

    if program.students.filter(id=student.id).exists():
        # If the student is already enrolled
        messages.error(request, "You are already enrolled in this program.")
    else:
        # Enroll the student in the program
        program.students.add(student)
        messages.success(request, "You have successfully enrolled in the program.")

    return redirect('training_programs', id=program.id)