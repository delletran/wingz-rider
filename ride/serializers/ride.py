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

    def validate(self, data):
        id_rider = data.get('id_rider')
        id_driver = data.get('id_driver')
        pickup_time = data.get('pickup_time')
        dropoff_time = data.get('dropoff_time')

        if id_rider == id_driver:
            raise serializers.ValidationError(
                "Rider and Driver cannot be the same.")

        if pickup_time and dropoff_time:
            if pickup_time >= dropoff_time:
                raise serializers.ValidationError(
                    "Dropoff time must be after pickup time.")

        return data
