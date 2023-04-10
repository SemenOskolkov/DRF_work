from django.urls import path

from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionListView, SubscriptionCreatAPIView, SubscriptionDestroyAPIView


app_name = SubscriptionConfig.name

urlpatterns = [
    path('', SubscriptionListView.as_view(), name='subscription_list'),
    path('create/', SubscriptionCreatAPIView.as_view(), name='subscription_create'),
    path('delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
]