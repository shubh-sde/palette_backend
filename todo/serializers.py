from rest_framework import serializers
from .models import Assignee,Resources,Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        depth = 1


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = "__all__"


class AssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignee
        fields = "__all__"