# Generated by Django 4.0.3 on 2022-05-28 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_student_sessions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teacher', to='app.teacher'),
        ),
    ]
