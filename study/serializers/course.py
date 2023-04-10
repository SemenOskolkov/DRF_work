from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from study.models import Course
from study.serializers.lesson import LessonListSerializer
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer
from users.models import User


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'name',
        )


class CourseDetailSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    numbers_lessons = serializers.SerializerMethodField()  # Для модели курса добавьте в сериализатор поле вывода количества уроков.
    lessons = LessonListSerializer(read_only=True, many=True)  # Для сериализатора для модели курса реализуйте поле вывода уроков.
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'name',
            'preview',
            'description',
            'owner',
            'numbers_lessons',
            'lessons',
            'subscription',
        )

    def get_numbers_lessons(self, instance):
        return instance.lessons.count()

    def get_subscription(self, course):
        user = self.context.get('request').user.id
        subscription_object = Subscription.objects.filter(user=user).filter(course=course).status
        return subscription_object