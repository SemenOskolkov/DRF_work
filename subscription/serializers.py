from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from study.models import Course
from subscription.models import Subscription
from users.models import User


class SubscriptionSerializer(serializers.ModelSerializer):
    student = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    course = SlugRelatedField(slug_field="name", queryset=Course.objects.all())

    class Meta:
        model = Subscription
        fields = (
            'user',
            'course',
            'status',
        )