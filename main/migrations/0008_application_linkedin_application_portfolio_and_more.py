# Generated by Django 5.1 on 2024-10-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_student_degree_alter_student_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='portfolio',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]
