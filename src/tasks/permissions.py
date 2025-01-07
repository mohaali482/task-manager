from django.contrib.auth.models import User 
from rest_framework import permissions

from .models import Task

class TaskOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Task):
        user: User = request.user
        if not user:
            return False
        
        if user.is_staff:
            return True
        
        return user == obj.user
