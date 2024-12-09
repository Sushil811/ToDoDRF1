from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class ToDoItemCreateView(generics.CreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [IsAuthenticated]

class ToDoItemDetailView(generics.RetrieveAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [IsAuthenticated]

class ToDoItemListView(generics.ListAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [IsAuthenticated]

class ToDoItemUpdateView(generics.UpdateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [IsAuthenticated]

class ToDoItemDeleteView(generics.DestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [IsAuthenticated]
