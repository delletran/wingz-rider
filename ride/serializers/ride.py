from rest_framework import serializers

from user.serializers.user import BaseUserSerializer

from ..models import Ride


class BaseRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            'id_ride',
            'status',
            'pickup_latitude',
            'pickup_longitude',
            'dropoff_latitude',
            'dropoff_longitude',
            'pickup_time',
            'dropoff_time',
        ]


class RideSerializer(BaseRideSerializer):
    rider = BaseUserSerializer(source='id_rider')
    driver = BaseUserSerializer(source='id_driver')

    class Meta:
        model = Ride
        fields = [
            'rider',
            'driver',
        ]


class RideUpsertSerializer(BaseRideSerializer):

    class Meta:
        model = Ride
        fields = [
            'id_rider',
            'id_driver',
        ] + BaseRideSerializer.Meta.fields
