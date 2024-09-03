from django.urls import path

from .views import UserRegister

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', UserRegister.as_view(), name = 'user_register'),
    path('sign-in', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signin-refresh', TokenRefreshView.as_view(), name='token_refresh'),
]