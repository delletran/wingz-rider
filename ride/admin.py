from django.contrib import admin
from .models import Ride, RideEvent


class RideAdmin(admin.ModelAdmin):
    list_display = ('id_ride', 'status', 'id_rider', 'id_driver',
                    'pickup_latitude', 'pickup_longitude', 'pickup_time', 'dropoff_time')
    search_fields = ('id_rider__username', 'id_driver__username', 'status')
    list_filter = ('status', 'pickup_time', 'dropoff_time')
    ordering = ['-pickup_time', '-id_ride']
    # fieldsets = (
    #     ('General Information', {
    #         'fields': ('id_ride', 'status', 'id_rider', 'id_driver')
    #     }),
    #     ('Location Information', {
    #         'fields': ('pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude')
    #     }),
    #     ('Time Information', {
    #         'fields': ('pickup_time', 'dropoff_time')
    #     }),
    # )

    readonly_fields = ('id_ride',)


class RideEventAdmin(admin.ModelAdmin):
    list_display = ('id_ride_event', 'id_ride', 'description', 'created_at')
    search_fields = ('id_ride__id_ride', 'description')
    list_filter = ('created_at',)
    # fieldsets = (
    #     ('General Information', {
    #         'fields': ('id_ride', 'description', 'created_at')
    #     }),
    # )

    readonly_fields = ('id_ride_event', 'created_at')


admin.site.register(Ride, RideAdmin)
admin.site.register(RideEvent, RideEventAdmin)
