from django.urls import path, include
from apps.users.views import hello_world, UsersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UsersViewSet, basename='user')

urlpatterns = [
    path('test_users/', hello_world, name="test_users"),
    path('', include(router.urls))
]
