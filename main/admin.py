from django.contrib import admin

# Register your models here.
from .models import*

admin.site.register(StudentPerformance)
admin.site.register(Student)
admin.site.register(Skill)
admin.site.register(Company)
admin.site.register(JobPost)
admin.site.register(TrainingProgram)
admin.site.register(Application)
admin.site.register(Feedback)