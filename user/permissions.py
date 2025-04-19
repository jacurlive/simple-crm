from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model


User = get_user_model()


class IsAdminRole(BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return

        try:
            employee = User.objects.get(username=request.user.username)
            employee_role = str(employee.employee_role)

            if employee_role == "Admin":
                return employee.is_active

        except User.DoesNotExist:
            return False
