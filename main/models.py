from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=15, unique=True)
    department = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    resume = models.FileField(upload_to='resumes/')
    skills = models.ManyToManyField('Skill', related_name='students')

    def __str__(self):
        return self.user.username
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name        
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
class JobPost(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField()
    required_skills = models.ManyToManyField('Skill', related_name='job_posts')
    eligibility_criteria = models.TextField()
    
    def __str__(self):
        return f"{self.title} at {self.company.name}"
class TrainingProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    instructor = models.CharField(max_length=255)
    skills_taught = models.ManyToManyField(Skill, related_name='training_programs')
    students = models.ManyToManyField(Student, related_name='training_programs')
    prerequisite_skills = models.ManyToManyField(Skill, related_name='required_for_trainings', blank=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='applications')
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Applied', 'Applied'), ('Shortlisted', 'Shortlisted'), ('Interviewed', 'Interviewed'), ('Rejected', 'Rejected'), ('Hired', 'Hired')], default='Applied')
    interview_date = models.DateTimeField(null=True, blank=True)
    interview_feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.job_post.title}"


class PlacementEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    companies = models.ManyToManyField(Company, related_name='placement_events')
    students = models.ManyToManyField(Student, related_name='placement_events')

    def __str__(self):
        return self.title
class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='feedbacks', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='feedbacks', null=True, blank=True)
    placement_event = models.ForeignKey(PlacementEvent, on_delete=models.CASCADE, related_name='feedbacks', null=True, blank=True)
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE, related_name='feedbacks', null=True, blank=True)
    content = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Feedback by {self.student.user.username if self.student else self.company.name}"
class StudentPerformance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='performances')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='performances')
    interview_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    improvement_suggestions = models.TextField(null=True, blank=True)
    suggested_trainings = models.ManyToManyField(TrainingProgram, related_name='suggested_to_students')

    def __str__(self):
        return f"Performance for {self.student.user.username} on {self.application.job_post.title}"