from django.urls import path, include
from apps.users.views import hello_world, UsersViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
  TokenVerifyView
)

router = DefaultRouter()
router.register(r'', UsersViewSet, basename='user')

urlpatterns = [
    path('test_users/', hello_world, name="test_users"),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include(router.urls)),
]
