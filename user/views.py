from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from core.permissions import IsAdminUser
from user.serializers.token import AuthTokenObtainPairSerializer

from .models import User
from .serializers.user import (BaseUserSerializer, UserSerializer,
                               UserUpsertSerializer)

User = get_user_model()


class UserCreateView(CreateAPIView):
    serializer_class = UserUpsertSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserUpdateView(UpdateAPIView):
    serializer_class = UserUpsertSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "first_name": ['exact'],
        "last_name": ['exact'],
    }
    search_fields = ['first_name', 'last_name']


class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserDestroyView(DestroyAPIView):
    serializer_class = BaseUserSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class AuthTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer
