# Generated by Django 4.0.3 on 2022-05-22 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_student_sessions_student_teacher_alter_session_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='sessions',
        ),
    ]