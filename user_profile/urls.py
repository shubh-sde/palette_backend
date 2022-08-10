from django.urls import path
from .views.profile_view import profile_list_view,profile_update_view

urlpatterns = [
      path('', profile_list_view),
      path('update/<int:pk>',profile_update_view),
]