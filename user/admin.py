from django.apps import apps
from django.contrib import admin

from .models import User

# admin.site.register(apps.all_models['user'].values())




@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'role',
        'is_superuser',
    )
    search_fields = ('email', 'firstname', 'lastname')
    ordering = ('-pk',)
