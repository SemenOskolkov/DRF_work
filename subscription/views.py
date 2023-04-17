from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from study.models import Course
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer


# class SubscriptionListView(generics.ListAPIView):
#     serializer_class = SubscriptionSerializer
#     queryset = Subscription.objects.all()
#
#
# class SubscriptionCreatAPIView(generics.CreateAPIView):
#     serializer_class = SubscriptionSerializer
#
#
# class SubscriptionDestroyAPIView(generics.DestroyAPIView):
#     serializer_class = SubscriptionSerializer
#     queryset = Subscription.objects.all()


class SubscriptionAPIView(APIView):

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        subscription_item = Subscription.objects.filter(user=user, course=course_item)

        if subscription_item.exists():
            subscription_item.delete()
            message = f'Подписка удалена'

        else:
            Subscription.objects.create(user=user, course=course_item)
            message = f'Подписка добавлена'

        return Response({'message': message})
