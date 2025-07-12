from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Department, Position, WorkSchedule, Task, PayrollRecord


User = get_user_model()


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"


    def create(self, validated_data):
        groups = validated_data.pop('groups', [])
        permissions = validated_data.pop('user_permissions', [])
        password = validated_data.pop("password")

        employee = User(**validated_data)
        employee.set_password(password)
        employee.save()

        employee.groups.set(groups)
        employee.user_permissions.set(permissions)

        return employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class PayrollRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollRecord
        fields = "__all__"
