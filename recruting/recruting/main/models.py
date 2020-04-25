from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, UserManager
from rest_framework import serializers

from recruting.skills.models import Position, SkillSet, Category
from recruting.utils.validators import validate_file_size


def validate_role(value):
    if 3 < value < 0:
        return serializers.ValidationError('invalid number of Role')


class MyUser(AbstractUser):
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MANAGER, 'manager'),
        (EMPLOYEE, 'employee')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, validators=[validate_role])
    # image = models.ImageField(upload_to='media',
    #                           validators=[validate_file_size],
    #                           null=True, blank=True)

    # attachment = models.FileField(upload_to='attachments',
    #                               validators=[validate_file_size],
    #                               null=True, blank=True)

    def __str__(self):
        return f'({self.id}) {self.username} {self.first_name} {self.last_name}'


class MyUserManager(UserManager):
    def get_admin(self):
        return self.filter(role=1)

    def get_manager(self):
        return self.filter(role=2)

    def get_office_employee(self):
        return self.filter(role=3)


class Admin(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

    objects = MyUserManager()

    def __str__(self):
        return f'{self.id} {self.user}'


class Manager(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = MyUserManager()

    def __str__(self):
        return f'Manager: {self.id} {self.user} {self.department}'


class Employee(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='positions')

    # attachment = models.FileField(upload_to='attachments',
    #                               validators=[validate_file_size],
    #                               null=True, blank=True)

    # image = models.ImageField(upload_to='media',
    #                           validators=[validate_file_size],
    #                           null=True, blank=True)

    objects = MyUserManager()

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f'Employee: {self.id} {self.user} {self.position}'


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(SkillSet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee} {self.skill}'


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)