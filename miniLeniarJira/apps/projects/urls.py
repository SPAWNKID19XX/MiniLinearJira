from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, hello_world

router = DefaultRouter()
router.register(r"", ProjectViewSet, basename="projects")


urlpatterns = [
    path('test_project/', hello_world, name="test_users"),
    path('', include(router.urls)),
]