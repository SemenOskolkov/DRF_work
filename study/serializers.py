from rest_framework import serializers

from study.models import Course, Lesson
from study.validators import LinkVideoValidator
from subscription.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    validators = [LinkVideoValidator(field='link_to_video')]

    class Meta:
        model = Lesson
        fields = (
            'name',
            'preview',
            'description',
            'link_to_video',
        )


class CourseSerializer(serializers.ModelSerializer):
    numbers_lessons = serializers.SerializerMethodField()  # Для модели курса добавьте в сериализатор поле вывода количества уроков.
    lessons = LessonSerializer(many=True, source='lesson_set')  # Для сериализатора для модели курса реализуйте поле вывода уроков.
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'name',
            'preview',
            'description',
            'numbers_lessons',
            'subscription',
        )

    def get_numbers_lessons(self, instance):
        return instance.lessons.count()

    def get_subscription(self, instance):
        subscription_object = Subscription.objects.filter(course=instance).order_by('id')
        if subscription_object:
            return subscription_object.status
