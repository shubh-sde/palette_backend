from tkinter.tix import Tree
from django.conf import settings
from django.db import models

class Assignee(models.Model):
    assignee_name = models.CharField(max_length=80)
    assignee_pic_url = models.URLField()

class Resources(models.Model):
    resource_name = models.CharField(max_length=80)
    resource_pic_url = models.URLField()


User = settings.AUTH_USER_MODEL

class Todo(models.Model):
    assignees = models.ManyToManyField(Assignee)
    type = models.CharField(max_length=80,null=True)
    expiration_date = models.DateField()
    expiration_time = models.TimeField()
    listed_by = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    action_text = models.CharField(max_length=150,null=True)
    description = models.TextField(null=True)
    resources = models.ManyToManyField(Resources)
    created_date = models.DateTimeField(null=True)
    