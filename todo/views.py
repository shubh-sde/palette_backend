from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated


class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # title = serializer.validated_data.get('title')
        # content = serializer.validated_data.get('content')
        # if content is None:
        #     content = title
        serializer.save()#content=content)

    def get_queryset(self):
        user = self.request.user
        record = Todo.objects.filter(listed_by=user)
        if record is None or record == "":
            return "No Data Found"
        return record

todo_list_view = TodoListView.as_view()