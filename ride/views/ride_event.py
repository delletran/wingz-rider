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
from ..models import RIDE_STATUS, RideEvent
from ..serializers.ride_event import (BaseRideEventSerializer,
                                      RideEventDropOffSerializer,
                                      RideEventPickUpSerializer,
                                      RideEventSerializer,
                                      RideEventUpsertSerializer)


class RideEventPickUpView(CreateAPIView):
    serializer_class = RideEventPickUpSerializer
    queryset = RideEvent.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            ride_event: RideEvent = serializer.save()

            ride_event.update_ride_status(RIDE_STATUS.PICKUP)

            return Response({
                'message': ride_event.description,
                'ride_event': RideEventSerializer(ride_event).data
            }, status=status.HTTP_201_CREATED)


class RideEventDropOffView(UpdateAPIView):
    serializer_class = RideEventDropOffSerializer
    queryset = RideEvent.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def update(self, request, *args, **kwargs):
        with transaction.atomic():
            response = super().update(request, *args, **kwargs)
            ride_event: RideEvent = self.get_object()

            ride_event.update_ride_status(RIDE_STATUS.DROPOFF)

            return Response({
                'message': ride_event.description,
                'ride_event': RideEventSerializer(ride_event).data
            }, status=status.HTTP_200_OK)


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
