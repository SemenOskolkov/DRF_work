from rest_framework import serializers

from study.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

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
    lessons = LessonSerializer(many=True)  # Для сериализатора для модели курса реализуйте поле вывода уроков.

    class Meta:
        model = Course
        fields = (
            'name',
            'preview',
            'description',
            'numbers_lessons',
        )

    def get_numbers_lessons(self, instance):
        return instance.lessons.count()
