# from rest_framework import serializers
#
# from study.models import Course, Lesson
# from study.validators import LinkVideoValidator
# from subscription.models import Subscription
# from subscription.serializers import SubscriptionSerializer
#
#
# class LessonSerializer(serializers.ModelSerializer):
#     validators = [LinkVideoValidator(field='link_to_video')]
#
#     class Meta:
#         model = Lesson
#         fields = (
#             'name',
#             'preview',
#             'description',
#             'link_to_video',
#         )
#
#
# class LessonInfoSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Lesson
#         fields = (
#             'name',
#         )
#
#
# class CourseSerializer(serializers.ModelSerializer):
#     numbers_lessons = serializers.SerializerMethodField()  # Для модели курса добавьте в сериализатор поле вывода количества уроков.
#     lessons = LessonInfoSerializer(read_only=True, many=True)  # Для сериализатора для модели курса реализуйте поле вывода уроков.
#     subscription = SubscriptionSerializer()
#
#     class Meta:
#         model = Course
#         fields = (
#             'name',
#             'preview',
#             'description',
#             'numbers_lessons',
#             'lessons',
#             'subscription',
#         )
#
#     def get_numbers_lessons(self, instance):
#         return instance.lessons.count()

    # def get_subscription(self, instance):
    #     subscription_object = Subscription.objects.filter(course=instance).order_by('id')
    #     if subscription_object:
    #         return subscription_object.status
