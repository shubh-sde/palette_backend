from django.urls import path
from .views.profile_view import profile_list_view

urlpatterns = [
      path('', profile_list_view),
]