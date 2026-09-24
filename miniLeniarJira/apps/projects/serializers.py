from rest_framework import serializers
from .models import Project, ProjectMember
from apps.users.serializers import UserSerializer
from django.db import transaction

class ProjectSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields = ['id', 'name', 'description']

  def create(self, validated_data):
    with transaction.atomic():
      new_project = Project.objects.create(
        **validated_data
      )
      ProjectMember.objects.create(
        project=new_project,
        user = self.context["request"].user,
        role = "owner"
      )
    return new_project

class ProjectMemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectMember
    fields = ['id', 'project', 'user', 'role']
