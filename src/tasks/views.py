from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions

from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer
from .permissions import TaskOwnerOrAdmin

class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, TaskOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status", "created_at"]
    search_fields = ["title"]

    def get_queryset(self):
        request = self.request
        user = request.user

        if user.is_staff:
            return Task.objects.all()
        
        return Task.objects.filter(user__id=user.id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated, TaskOwnerOrAdmin]
    serializer_class = TaskUpdateSerializer
    http_method_names = ["patch"]
