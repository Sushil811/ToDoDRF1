from django.urls import path
from .views import (
    ToDoItemCreateView,
    ToDoItemDetailView,
    ToDoItemListView,
    ToDoItemUpdateView,
    ToDoItemDeleteView
)

urlpatterns = [
    path('create/', ToDoItemCreateView.as_view(), name='todo-create'),
    path('<int:pk>/', ToDoItemDetailView.as_view(), name='todo-detail'),
    path('', ToDoItemListView.as_view(), name='todo-list'),
    path('update/<int:pk>/', ToDoItemUpdateView.as_view(), name='todo-update'),
    path('delete/<int:pk>/', ToDoItemDeleteView.as_view(), name='todo-delete'),
]
