# Generated by Django 4.0.3 on 2022-05-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_studentreporter_attend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreporter',
            name='attend',
            field=models.CharField(choices=[(0, 'حضور'), (1, 'غياب'), (3, 'لم يتم التحديد')], default='لم يتم التحديد', max_length=15, null=True),
        ),
    ]
