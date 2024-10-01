from django.urls import path

from ..views.ride import (RideCreateBookingView, RideDestroyView,
                          RideDetailView, RideListView, RideUpdateBookingView)

app_name = 'ride'

urlpatterns = [
    path('list',
         RideListView.as_view(), name='ride-list'),
    path('create',
         RideCreateBookingView.as_view(), name='ride-create'),
    path('<pk>/update',
         RideUpdateBookingView.as_view(), name='ride-update'),
    path('<pk>/delete',
         RideDestroyView.as_view(), name='ride-delete'),
    path('<pk>',
         RideDetailView.as_view(), name='ride-detail'),
]
