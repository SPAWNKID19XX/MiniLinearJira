from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet 
from .serializers import ProjectSerializer
from .models import Project



def hello_world(requests):
  print(requests)
  return HttpResponse("Hello World from Test Projects!")

# Create your views here.
class ProjectViewSet(ModelViewSet):
  serializer_class = ProjectSerializer


  
  


