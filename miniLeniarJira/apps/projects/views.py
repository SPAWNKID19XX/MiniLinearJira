from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet 
from .serializers import ProjectSerializer
from .permissions import IsProjectsAdmin
from .models import Project, ProjectMember



def hello_world(requests):
  print(requests)
  return HttpResponse("Hello World from Test Projects!")

# Create your views here.
class ProjectViewSet(ModelViewSet):
  serializer_class = ProjectSerializer
  permission_classes = [IsProjectsAdmin]

  def get_queryset(self):
    my_projects = ProjectMember.objects.filter(
      user = self.request.user.id
    ).values_list(
      "project_id",flat=True
    )
    return Project.objects.filter(id__in=my_projects)