from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from study.models import Lesson
from study.validators import LinkVideoValidator
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    validators = [LinkVideoValidator(field='link_to_video')]

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = (
            'name',
        )


class LessonDetailSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Lesson
        fields = (
            'name',
            'preview',
            'description',
            'link_to_video',
            'owner',
        )
