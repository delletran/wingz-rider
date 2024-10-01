from rest_framework import serializers

from ride.serializers.ride import BaseRideSerializer, RideUpsertSerializer

from ..models import Ride, RideEvent


class BaseRideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = [
            'id_ride_event',
        ]


class RideEventSerializer(BaseRideEventSerializer):
    ride = BaseRideSerializer(source='id_ride')

    class Meta:
        model = RideEvent
        fields = [
            'ride',
            'created_at',
            'description',
        ]


class RideEventUpsertSerializer(BaseRideEventSerializer):
    ride_data = RideUpsertSerializer(write_only=True)

    class Meta:
        model = RideEvent
        fields = [
            'ride_data',
        ] + BaseRideEventSerializer.Meta.fields

    def create(self, validated_data):
        ride_data = validated_data.pop('ride_data', None)

        if ride_data:
            ride_instance = Ride.objects.create(**ride_data)
            validated_data['id_ride'] = ride_instance

        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        ride_data = validated_data.pop('ride_data', None)

        if ride_data:
            ride_instance = instance.id_ride
            for attr, value in ride_data.items():
                setattr(ride_instance, attr, value)
            ride_instance.save()

        instance = super().update(instance, validated_data)
        return instance
