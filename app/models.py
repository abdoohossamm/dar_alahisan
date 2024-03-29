from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

def only_int(value):
    if value.isdigit()==False:
        raise ValidationError('تم وضع حروف بدلا من ارقام برجاء التصحيح')


class Manager(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم الموظف')
    n_id = models.CharField(max_length= 14, verbose_name='الرقم القومى', validators= [validators.MinLengthValidator(14, 'الرقم القومى يجب ان يكون 14 رقم'), only_int])
    address= models.CharField(max_length= 150)
    phone= models.CharField(max_length= 12, validators= [validators.MinLengthValidator(11,
                                        'رقم الهاتف يجب ان يكون 11رقم'),
                                            only_int])
    home_number = models.CharField(max_length= 12)
    salary =models.DecimalField(max_digits=10, decimal_places=2, blank= True, null=True)
    class Meta:
        unique_together = ['n_id', 'phone']
    def __str__(self):
        return self.name
    
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=150)
    n_id = models.CharField(max_length= 14)
    address= models.CharField(max_length= 150)
    phone= models.CharField(max_length= 12, validators= [validators.MinLengthValidator(11,
                                        'رقم الهاتف يجب ان يكون 11رقم'),
                                            only_int])
    home_number = models.CharField(max_length= 12)
    class Meta:
        unique_together = ['n_id', 'phone']
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=150, unique=True)
    branch = models.ForeignKey(Branch, related_name='branch_room', on_delete=models.PROTECT)
    def __str__(self):
        return self.name


class Day(models.Model):
    day = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return self.day
    
    
class Session(models.Model):
    day = models.ForeignKey(Day, related_name='session', on_delete=models.PROTECT)
    time = models.TimeField()
    name = models.ForeignKey(Room, related_name= 'room', null=True, on_delete=models.SET_NULL,blank= True)
    teacher = models.ForeignKey(Teacher, related_name= 'teacher', on_delete=models.PROTECT, null= True)
    class Meta:
        unique_together = ['day', 'time', 'teacher']
    def __str__(self):
        return (f'{self.teacher.name} غرفة {self.name} يوم {self.day} الساعة {self.time}') # type: ignore
    
    
class Student(models.Model):
    name = models.CharField(max_length=150)
    n_id = models.CharField(max_length= 14)
    address= models.CharField(max_length= 150)
    phone= models.CharField(max_length= 12, validators= [validators.MinLengthValidator(11, 'رقم الهاتف يجب ان يكون 11رقم'), only_int])
    home_number = models.CharField(max_length= 12)
    teacher = models.ForeignKey(Teacher, related_name="student_teacher" ,on_delete=models.PROTECT, blank= True, null= True)
    class Meta:
        unique_together = ['n_id', 'phone']
    def __str__(self):
        return f'{self.name}'
    
    
class StudentSessions(models.Model):
    student = models.ForeignKey(Student, related_name='student_session', on_delete=models.CASCADE)
    session = models.ForeignKey(Session, related_name='student_session', on_delete=models.CASCADE)
    class Meta:
        unique_together = ['student', 'session']
    def __str__(self):
        return f'{self.student.name}, {self.session.teacher}, {self.session.time}, {self.session.name} '  # type: ignore


