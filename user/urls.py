from django.urls import path

from .views import (UserCreateView, UserDestroyView, UserDetailView,
                    UserListView, UserUpdateView)

app_name = 'user'

urlpatterns = [

    path('list',
         UserListView.as_view(), name='user-list'),
    path('create',
         UserCreateView.as_view(), name='user-create'),
    path('<pk>/update',
         UserUpdateView.as_view(), name='user-update'),
    path('<pk>/delete',
         UserDestroyView.as_view(), name='user-delete'),
    path('<pk>',
         UserDetailView.as_view(), name='user-detail'),
]
