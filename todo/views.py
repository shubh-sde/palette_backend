from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # title = serializer.validated_data.get('title')
        # content = serializer.validated_data.get('content')
        # if content is None:
        #     content = title
        serializer.save()#content=content)

todo_list_view = TodoListView.as_view()