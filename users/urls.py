from django.urls import path

from users.apps import UsersConfig
from users.views import UserListView, UserCreatAPIView, UserUpdateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/create/', UserCreatAPIView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
]