from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListView, UserCreatAPIView, UserUpdateAPIView, UserRetrieveAPIView


app_name = UsersConfig.name


urlpatterns = [
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/create/', UserCreatAPIView.as_view(), name='user_create'),
    path('user/profile/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]