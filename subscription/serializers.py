from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from study.models import Course
from subscription.models import Subscription
from users.models import User


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = (
            'user',
            'course',
            'status',
        )