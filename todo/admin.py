from django.contrib import admin
from .models import Todo,Assignee,Resources

# Register your models here.
admin.site.register(Todo)
admin.site.register(Assignee)
admin.site.register(Resources)