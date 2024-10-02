from django.db.models.manager import BaseManager
from rest_framework import serializers

from ride.serializers.ride import (RidePickUpSerializer, RideSerializer,
                                   RideUpsertSerializer)

from ..models import Ride, RideEvent


class BaseRideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = [
            'id_ride_event',
        ]


class RideEventSerializer(BaseRideEventSerializer):
    ride = RideSerializer(source='id_ride')

    class Meta:
        model = RideEvent
        fields = [
            'ride',
            'created_at',
            'description',
        ] + BaseRideEventSerializer.Meta.fields


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


class RideEventPickUpSerializer(serializers.ModelSerializer):
    ride_data = RidePickUpSerializer(write_only=True)

    class Meta:
        model = RideEvent
        fields = [
            'id_ride',
            'ride_data',
        ]

    def create(self, validated_data):
        ride_instance: Ride = validated_data.get('id_ride', None)
        ride_data = validated_data.pop('ride_data', None)
        id_driver = ride_data.get('id_driver', None)

        instance = super().create(validated_data)

        if id_driver:
            ride_instance.id_driver = id_driver
            ride_instance.save()

        return instance

    def validate(self, attrs):
        ride_instance: Ride = attrs.get('id_ride', None)
        ride_events: BaseManager[RideEvent] = ride_instance.ride_events.all()

        id_ride: Ride = attrs.get('id_ride')
        ride_data = attrs.get('ride_data')
        id_driver = ride_data.get('id_driver')

        if ride_events:
            raise serializers.ValidationError(
                "Booking/Ride has already been pickup by another driver.")

        if id_ride and id_ride.id_rider == id_driver:
            raise serializers.ValidationError(
                "Rider and Driver cannot be the same.")

        return super().validate(attrs)

    def update(self, instance, validated_data):
        ride_data = validated_data.pop('ride_data', None)

        instance = super().update(instance, validated_data)
        return instance


class RideEventDropOffSerializer(serializers.ModelSerializer):

    class Meta:
        model = RideEvent
        fields = []
