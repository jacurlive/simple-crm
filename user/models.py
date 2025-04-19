from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

from django.db.models import PROTECT
from multiselectfield import MultiSelectField
from django.utils import timezone


class Department(models.Model):
    objects = None
    name = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    objects = None
    name = models.CharField(max_length=55)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"


class WorkSchedule(models.Model):
    objects = None
    DAYS_OF_WEEK = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]

    name = models.CharField(max_length=255)
    day_of_week = MultiSelectField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name}"


class Role(models.Model):
    role_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.role_name}"


class Employee(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(default=date.today)
    hire_date = models.DateField(default=date.today)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=PROTECT, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=PROTECT, null=True, blank=True)
    work_schedule = models.ForeignKey('WorkSchedule', on_delete=PROTECT, blank=True, null=True)
    employee_role = models.ForeignKey('Role', on_delete=PROTECT, blank=True, null=True)
    employee_card = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.status} - {self.assign_to}"


class PayrollRecord(models.Model):
    TRANSACTION_TYPES = [
        ('bonus', 'Bonus'),
        ('fine', 'Fine'),
        ('advance', 'Advance'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payroll_record')
    month = models.DateField(default=timezone.now)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
