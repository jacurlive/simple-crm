from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Employee, Department, Position, WorkSchedule, Task, PayrollRecord
from .permissions import IsAdminRole
from .serializers import EmployeeSerializer, DepartmentSerializer, PositionSerializer, WorkScheduleSerializer, \
    TaskSerializer, PayrollRecordsSerializer


class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)


class EmployeeAPICreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminRole,)


class EmployeeAPIDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)


class EmployeeAPIUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminRole,)


class DepartmentAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,)


class DepartmentAPICreateView(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAdminRole,)


class DepartmentAPIDetailView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,)


class DepartmentAPIUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAdminRole,)


class PositionAPIView(generics.ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (IsAuthenticated,)


class PositionAPICreateView(generics.CreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (IsAdminRole,)


class PositionAPIDetailView(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (IsAuthenticated,)


class PositionAPIUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (IsAdminRole,)


class WorkScheduleAPIView(generics.ListCreateAPIView):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
    permission_classes = (IsAdminRole,)


class WorkScheduleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
    permission_classes = (IsAdminRole,)


class TaskAPIListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(assign_to=self.request.user)


class TaskAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(assign_to=self.request.user)


class PayrollRecordsView(generics.ListAPIView):
    queryset = PayrollRecord.objects.all()
    serializer_class = PayrollRecordsSerializer


class PayrollRecordsByUserIDView(generics.ListAPIView):
    queryset = PayrollRecord
    serializer_class = PayrollRecordsSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return PayrollRecord.objects.filter(employee=user_id)
