"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import json

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from user.views import AuthTokenObtainPairView

urlpatterns = [

    path('api/token/', AuthTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("api/user/", include('user.urls')),

]


if settings.DEBUG:
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view

    from base.utils.read_write_file import read_file

    api_info_dump = read_file('base/constants/api_info.json')
    api_info = json.loads(api_info_dump)

    schema_view = get_schema_view(
        openapi.Info(
            title='Wingz Rider APIs',
            default_version='v1',
            description=api_info['description'],
            terms_of_service="/terms/",
            contact=openapi.Contact(email="Rider.wingz@gmail.com"),
            license=openapi.License(name="Rider Wingz License"),
        ),
        public=True,
        permission_classes=(permissions.IsAdminUser,)
    )
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('swagger/', schema_view.with_ui(
            'swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui(
            'redoc', cache_timeout=0), name='schema-redoc'),
    ]
