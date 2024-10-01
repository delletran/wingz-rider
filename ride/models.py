
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RIDE_STATUS(models.TextChoices):
    ENROUTE = 'en-route', 'En Route'
    PICKUP = 'pickup', 'Pickup'
    DROPOFF = 'dropoff', 'Dropoff'


class Ride(models.Model):

    class Meta:
        db_table = 'db_ride'
        verbose_name = "Ride"
        verbose_name_plural = "Rides"
        ordering = ['-pickup_time', '-pk']

    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(
        max_length=10,
        choices=RIDE_STATUS.choices,
        default=RIDE_STATUS.PICKUP
    )
    id_rider = models.ForeignKey(
        User,
        related_name='rider_rides',
        on_delete=models.CASCADE
    )
    id_driver = models.ForeignKey(
        User,
        related_name='driver_rides',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField(blank=True, null=True)
    dropoff_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.pk} | {self.status}'


class RideEvent(models.Model):

    class Meta:
        db_table = 'db_ride_event'
        verbose_name = 'Ride Event'
        verbose_name_plural = 'Ride Events'
        ordering = ['-created_at']

    id_ride_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey(
        Ride,
        related_name='ride_events',
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def update_ride_status(self, _status: RIDE_STATUS.choices):
        with transaction.atomic():
            if _status == RIDE_STATUS.PICKUP:
                self.id_ride.pickup_time = timezone.now()
            elif _status == RIDE_STATUS.DROPOFF:
                self.id_ride.dropoff_time = timezone.now()

            self.id_ride.status = _status
            self.description = f"Status changed to {_status}."

            self.id_ride.save()
            self.save()

    def __str__(self):
        return f'{self.pk} | {self.id_ride.id_ride} - {self.description[:50]}'
