from django.urls import path
from .views import TaskListCreateView, TaskDetailView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list'),
    path('<int:id>/', TaskDetailView.as_view(), name='task-detail'),
]