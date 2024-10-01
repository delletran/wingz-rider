from django.urls import path

from ..views.ride_event import (RideEventDestroyView, RideEventDetailView,
                                RideEventDropOffView, RideEventListView,
                                RideEventPickUpView, RideEventUpdateView)

app_name = 'ride_event'

urlpatterns = [
    path('list',
         RideEventListView.as_view(), name='ride_event-list'),
    path('pickup',
         RideEventPickUpView.as_view(), name='ride_event-pickup'),
    path('<pk>/dropoff',
         RideEventDropOffView.as_view(), name='ride_event-dropoff'),
    path('<pk>/update',
         RideEventUpdateView.as_view(), name='ride_event-update'),
    path('<pk>/delete',
         RideEventDestroyView.as_view(), name='ride_event-delete'),
    path('<pk>',
         RideEventDetailView.as_view(), name='ride_event-detail'),
]
