# Generated by Django 4.0.3 on 2022-05-28 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_session_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teacher', to='app.teacher'),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='student_teacher', to='app.teacher'),
        ),
    ]
