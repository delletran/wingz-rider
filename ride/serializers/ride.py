from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.serializers.user import BaseUserSerializer

from ..models import Ride

User = get_user_model()


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
        ] + BaseRideSerializer.Meta.fields


class RideUpsertSerializer(BaseRideSerializer):
    id_driver = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Ride
        fields = [
            'id_ride',
            'id_rider',
            'id_driver',
            'status',
            'pickup_latitude',
            'pickup_longitude',
            'dropoff_latitude',
            'dropoff_longitude',
        ]

    def validate(self, data):
        id_rider = data.get('id_rider')
        id_driver = data.get('id_driver')

        if id_rider == id_driver:
            raise serializers.ValidationError(
                "Rider and Driver cannot be the same.")

        return data


class RidePickUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ride
        fields = [
            'id_ride',
            'id_driver',
        ]

    def validate(self, data):
        id_ride: Ride = data.get('id_ride')
        id_driver = data.get('id_driver')

        if id_ride and id_ride.id_rider == id_driver:
            raise serializers.ValidationError(
                "Rider and Driver cannot be the same.")

        return data
