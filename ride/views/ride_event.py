from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.permissions import IsAdminUser

from ..filterset import RideEventFilter
from ..models import RideEvent
from ..serializers.ride_event import (BaseRideEventSerializer,
                                      RideEventSerializer,
                                      RideEventUpsertSerializer)


class RideEventCreateView(CreateAPIView):
    serializer_class = RideEventUpsertSerializer
    queryset = RideEvent.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class RideEventUpdateView(UpdateAPIView):
    serializer_class = RideEventUpsertSerializer
    queryset = RideEvent.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class RideEventListView(ListAPIView):
    serializer_class = RideEventSerializer
    queryset = RideEvent.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RideEventFilter
    search_fields = [
        'id_ride__id_driver__first_name',
        'id_ride__id_driver__last_name'
    ]


class RideEventDetailView(RetrieveAPIView):
    serializer_class = RideEventSerializer
    queryset = RideEvent.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]


class RideEventDestroyView(DestroyAPIView):
    serializer_class = BaseRideEventSerializer
    queryset = RideEvent.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]
