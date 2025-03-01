from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.CreateTaskList.as_view(), name = "task-list"),
    path("tasks/delete/<int:pk>/", views.DeleteTask.as_view(), name="delete-note"),
]