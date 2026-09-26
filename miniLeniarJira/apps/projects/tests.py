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
