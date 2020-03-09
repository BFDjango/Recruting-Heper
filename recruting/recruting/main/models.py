from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser

from recruting.skills.models import Position, SkillSet, Category

from rest_framework import serializers


class MyUser(AbstractUser):
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MANAGER, 'employee'),
        (EMPLOYEE, 'employee')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True)

    def __str__(self):
        return f'({self.id}) {self.username} {self.first_name} {self.last_name}'


class Admin(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.user}'


class Manager(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Manager: {self.id} {self.user} {self.department}'


class Employee(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='positions')

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

