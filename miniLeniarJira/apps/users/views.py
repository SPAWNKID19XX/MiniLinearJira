from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import permissions
from django.http import HttpResponse

def hello_world(requests):
  print(requests)
  return HttpResponse("Hello World from Test users!")

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny]

  def get(self):
    return self.queryset
  
  