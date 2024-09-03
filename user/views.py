from rest_framework import generics,status, permissions
from rest_framework.response import Response
from .serializers import UserSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegister(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
