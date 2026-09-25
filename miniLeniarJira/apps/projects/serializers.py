from rest_framework import serializers
from .models import Project, ProjectMember
from django.db import transaction
from django.core.exceptions import PermissionDenied

class ProjectSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields = ['id', 'name', 'description']

  def create(self, validated_data):
    user = self.context["request"].user

    if not user.is_authenticated:
      raise PermissionDenied("Permission Danied. To create a new project you should be logged")
    
    with transaction.atomic():
      new_project = Project.objects.create(
        **validated_data
      )
      ProjectMember.objects.create(
        project=new_project,
        user = user,
        role = "owner"
      )
    return new_project
    
class ProjectMemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectMember
    fields = ['id', 'project', 'user', 'role']
