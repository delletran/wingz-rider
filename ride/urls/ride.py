from django.urls import path

from ..views.ride import (RideCreateView, RideDestroyView, RideDetailView,
                          RideListView, RideUpdateView)

app_name = 'ride'

urlpatterns = [
    path('list',
         RideListView.as_view(), name='ride-list'),
    path('create',
         RideCreateView.as_view(), name='ride-create'),
    path('<pk>/update',
         RideUpdateView.as_view(), name='ride-update'),
    path('<pk>/delete',
         RideDestroyView.as_view(), name='ride-delete'),
    path('<pk>',
         RideDetailView.as_view(), name='ride-detail'),
]
