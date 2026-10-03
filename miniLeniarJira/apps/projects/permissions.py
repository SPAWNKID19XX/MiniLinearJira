from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404
from .models import ProjectMember

class IsAdminOrOwner(BasePermission):

  def has_permission(self, request, view):
    return True

  def has_object_permission(self, request, view, obj):
    try:
      member_ship = obj.members.get(user=request.user)
      return member_ship.role in [ProjectMember.Role.ADMIN, ProjectMember.Role.OWNER]
    except ProjectMember.DoesNotExist:
      return False
