# Generated by Django 5.1 on 2024-10-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_jobpost_salary_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='job_requirements',
            field=models.TextField(default='none', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='job_responsibilities',
            field=models.TextField(default='none', max_length=1000),
            preserve_default=False,
        ),
    ]
