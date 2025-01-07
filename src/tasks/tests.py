from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from .views import TaskListCreateAPIView, TaskUpdateView
from .models import Task

class TaskTest(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = User.objects.create_superuser(
            username="testusername", email="test@test.com",
            password="testPassword123"
            )
        
        self.tasks = [
            {
                "user": self.user,
                "title": "Test Title 1",
                "description": "Test Description",
                "status": "pending",
            },
            {
                "user": self.user,
                "title": "Test Title 2",
                "description": "Test Description",
                "status": "pending",
            },
            {
                "user": self.user,
                "title": "Test Title 3",
                "description": "Test Description",
                "status": "in_progress",
            },
        ]
        for task in self.tasks:
            Task.objects.create(**task)
    
    def test_list_all(self):
        request = self.factory.get("/api/tasks")
        view = TaskListCreateAPIView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create(self):
        data = {"title": "Test title 4", "description": "description", "status": "pending"}
        request = self.factory.post("/api/tasks",data)
        view = TaskListCreateAPIView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 4)
    
    def test_update(self):
        test_status = 'complete'

        request = self.factory.patch("/api/tasks/1/set_state", {"status": test_status})
        view = TaskUpdateView.as_view()
        response = view(request, pk=1)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Task.objects.get(id=1).status, self.tasks[0].get("status"))

        force_authenticate(request, user=self.user)
        response = view(request, pk=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(Task.objects.get(id=1).status, self.tasks[0].get("status"))
        self.assertEqual(Task.objects.get(id=1).status, test_status)