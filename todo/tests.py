from django.test import TestCase
from .models import ToDoItem, Tag

class ToDoItemModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='Test')
        self.todo = ToDoItem.objects.create(
            title="Test Task",
            description="Test Description",
            due_date="2024-12-31",
        )
        self.todo.tags.add(self.tag)

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, "Test Task")
        self.assertEqual(self.todo.status, "OPEN")
