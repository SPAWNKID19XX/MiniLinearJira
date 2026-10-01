import pytest
from unittest.mock import patch
from rest_framework.test import APIClient

from apps.users.models import User
from apps.projects.models import Project, ProjectMember


@pytest.mark.django_db
def test_project_creation_rolls_back_if_member_creation_fails():
    user = User.objects.create_user(
        email="test@example.com",
        password="password123",
    )

    client = APIClient()
    client.force_authenticate(user=user)

    with patch(
        "apps.projects.serializers.ProjectMember.objects.create",
        side_effect=Exception("Member creation failed"),
    ):
        response = client.post(
            "/projects/",
            {
                "name": "Test Project",
                "description": "Test Description",
            },
            format="json",
        )

    assert Project.objects.count() == 0
    assert ProjectMember.objects.count() == 0

@pytest.mark.django_db
def test_permissions_to_get_project_queryset():
  user = User.objects.create_user(
    email="test@example.com",
    password="password123",
  )

  user1 = User.objects.create_user(
      email="test1@example.com",
      password="password123",
    )

  client = APIClient()
  client.force_authenticate(user=user)

  response = client.post(
    "/projects/api/v1/",
    {
        "name": "Test Project",
        "description": "Test Description",
    },
    format="json",
  )
  assert response.status_code == 201
  assert Project.objects.count() == 1
  assert ProjectMember.objects.count() == 1

  response = client.get(
      "/projects/api/v1/",
      format="json",
    )
  assert response.status_code == 200
  assert len(response.data) == 1
    
  client.force_authenticate(user=user1)

  response = client.get(
    "/projects/api/v1/",
    format="json",
  )

  assert response.status_code == 200
  assert len(response.data) == 0

@pytest.mark.django_db
def test_permissions_to_retreave_project_queryset():
  user = User.objects.create_user(
    email="test@example.com",
    password="password123",
  )

  user1 = User.objects.create_user(
      email="test1@example.com",
      password="password123",
    )

  client = APIClient()
  client.force_authenticate(user=user)

  response = client.post(
    "/projects/api/v1/",
    {
        "name": "Test Project",
        "description": "Test Description",
    },
    format="json",
  )
  assert response.status_code == 201

  id_project = response.data['id']

  response = client.get(
      f"/projects/api/v1/{id_project}/",
      format="json",
    )
  assert response.status_code == 200
    
  client.force_authenticate(user=user1)

  response = client.get(
    f"/projects/api/v1/{id_project}/",
    format="json",
  )

  assert response.status_code == 404