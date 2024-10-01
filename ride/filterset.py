
from django.utils.timezone import now, timedelta
from django_filters import BooleanFilter, FilterSet

from .models import Ride, RideEvent


class RideFilter(FilterSet):
    is_todays_ride_events = BooleanFilter(method='filter_todays_ride_events')

    class Meta:
        model = Ride
        fields = {
            "id_rider": ['exact'],
            "id_driver": ['exact'],
            "status": ['exact'],
            "id_rider__email": ['exact'],
        }


def filter_todays_ride_events(self, queryset, name, value):
    if value:
        last_24_hours = now() - timedelta(hours=24)
        queryset = queryset.filter(
            created_at__gte=last_24_hours
        )
    return queryset


class RideEventFilter(FilterSet):

    class Meta:
        model = RideEvent
        fields = {
            "id_ride_event": ['exact'],
            "id_ride": ['exact'],
        }
