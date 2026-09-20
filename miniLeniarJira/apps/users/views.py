from django.shortcuts import render
from rest_framework import viewsets
from config.settings import AUTH_USER_MODEL
from .serializers import UserSerializer
from rest_framework import permissions
from django.http import HttpResponse

def hello_world(requests):
  print(requests)
  return HttpResponse("Hello World from Test users!")

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
  queryset = AUTH_USER_MODEL.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny]

  def get(self):
    return self.queryset
  
  