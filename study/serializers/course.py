from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from study.models import Course
from study.serializers.lesson import LessonListSerializer
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
            'subscription',
            'lessons',
        )

    def get_numbers_lessons(self, instance):
        return instance.lessons.count()

    def _user(self):
        request = self.context.get('request', None)
        if request:
            return request.user
        return None

    def get_subscription(self, instance):
        return instance.subscription_set.filter(user=self._user).exists()
