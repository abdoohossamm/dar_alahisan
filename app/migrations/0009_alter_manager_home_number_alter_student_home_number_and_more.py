# Generated by Django 4.0.3 on 2022-08-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_session_teacher_alter_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='home_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='student',
            name='home_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='student',
            name='n_id',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='home_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='n_id',
            field=models.CharField(max_length=14),
        ),
    ]