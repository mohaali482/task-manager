from django.urls import path

from .views import TaskListCreateAPIView, TaskUpdateView 

urlpatterns = [
    path("tasks/", TaskListCreateAPIView.as_view()),
    path("tasks/<int:pk>/set_state", TaskUpdateView.as_view()),
]
