from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.permissions import IsAdminUser

from ..filterset import RideFilter
from ..models import Ride
from ..serializers.ride import (BaseRideSerializer, RideSerializer,
                                RideUpsertSerializer)


class RideCreateView(CreateAPIView):
    serializer_class = RideUpsertSerializer
    queryset = Ride.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class RideUpdateView(UpdateAPIView):
    serializer_class = RideUpsertSerializer
    queryset = Ride.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class RideListView(ListAPIView):
    serializer_class = RideSerializer
    queryset = Ride.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RideFilter
    search_fields = [
        'id_rider__email',
        'id_rider__first_name',
        'id_driver__last_name'
    ]
    ordering = ['pickup_time']


class RideDetailView(RetrieveAPIView):
    serializer_class = RideSerializer
    queryset = Ride.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class RideDestroyView(DestroyAPIView):
    serializer_class = BaseRideSerializer
    queryset = Ride.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]
