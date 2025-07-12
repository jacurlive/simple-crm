from django.urls import path

from .views import EmployeeAPIView, DepartmentAPIView, PositionAPIView, WorkScheduleAPIView, TaskAPIListView, \
    EmployeeAPIDetailView, TaskAPIDetailView, WorkScheduleAPIDetailView, EmployeeAPICreateView, \
    EmployeeAPIUpdateDestroyView, DepartmentAPICreateView, DepartmentAPIDetailView, DepartmentAPIUpdateView, \
    PositionAPICreateView, PositionAPIDetailView, PositionAPIUpdateView, PayrollRecordsView, PayrollRecordsByUserIDView

urlpatterns = [

    # Employee urls
    path('users/', EmployeeAPIView.as_view()),  # get
    path('users/create/', EmployeeAPICreateView.as_view()),  # post
    path('users/<int:pk>/', EmployeeAPIDetailView.as_view()),  # get
    path('users/update/<int:pk>/', EmployeeAPIUpdateDestroyView.as_view()),  # put-delete

    # Department urls
    path('department/', DepartmentAPIView.as_view()),  # get
    path('department/create/', DepartmentAPICreateView.as_view()),  # post
    path('department/<int:pk>/', DepartmentAPIDetailView.as_view()),  # get
    path('department/update/<int:pk>', DepartmentAPIUpdateView.as_view()),  # put-delete

    # Position urls
    path('position/', PositionAPIView.as_view()),  # get
    path('position/create/', PositionAPICreateView.as_view()),  # post
    path('position/<int:pk>/', PositionAPIDetailView.as_view()), # get
    path('position/update/<int:pk>/', PositionAPIUpdateView.as_view()),  # put-delete

    # Schedule urls
    path('schedule/', WorkScheduleAPIView.as_view()),  # get-post
    path('schedule/<int:pk>', WorkScheduleAPIDetailView.as_view()),  # get-put-delete

    # Task urls
    path('task/', TaskAPIListView.as_view()),  # get-post
    path('task/<int:pk>', TaskAPIDetailView.as_view()),  # get-put-delete

    # Payroll Records urls
    path('payrollrecords/', PayrollRecordsView.as_view()),  # get
    path('payrollrecords/user/<int:user_id>', PayrollRecordsByUserIDView.as_view()),  # get
]
