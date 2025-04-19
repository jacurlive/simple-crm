from django.contrib import admin
from .models import Employee, Department, Position, WorkSchedule, Task, Role, PayrollRecord


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "phone_number", "birth_date", "salary", "position", "department", "is_active", "employee_role")
    list_display_links = ("id", "username", "first_name", "last_name", "phone_number")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id", "name",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id", "name",)


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "start_time", "end_time")
    list_display_links = ("id", "name")


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "assign_to", "deadline", "status")
    list_display_links = ("id", "title", "assign_to", "deadline", "status")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "role_name")


@admin.register(PayrollRecord)
class PayrollRecord(admin.ModelAdmin):
    list_display = ("id", "employee", "month", "transaction_type", "amount", "description", "created_at")
    list_display_links = ("id", "employee", "month")
