# Generated by Django 4.0.3 on 2023-01-16 12:47

from django.db import migrations, models
import django.db.models.deletion
def populate_names(apps, schema_editor):
    names = ["جناكليس"]
    Branch = apps.get_model('app', 'Branch')
    for name in names:
        obj = Branch(name=name)
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_manager_home_number_alter_student_home_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.RunPython(populate_names),
        migrations.AddField(
            model_name='room',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='branch_room', to='app.branch'),
            preserve_default=False,
        ),

    ]