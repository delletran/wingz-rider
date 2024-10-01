from django.urls import path

from ..views.ride_event import (RideEventCreateView, RideEventDestroyView,
                                RideEventDetailView, RideEventListView,
                                RideEventUpdateView)

app_name = 'ride_event'

urlpatterns = [
    path('list',
         RideEventListView.as_view(), name='ride_event-list'),
    path('create',
         RideEventCreateView.as_view(), name='ride_event-create'),
    path('<pk>/update',
         RideEventUpdateView.as_view(), name='ride_event-update'),
    path('<pk>/delete',
         RideEventDestroyView.as_view(), name='ride_event-delete'),
    path('<pk>',
         RideEventDetailView.as_view(), name='ride_event-detail'),
]
