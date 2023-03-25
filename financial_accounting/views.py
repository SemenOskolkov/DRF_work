from django.shortcuts import render
from rest_framework import generics

from financial_accounting.models import Payment
from financial_accounting.serializers import PaymentCourseSerializer, PaymentLessonSerializer


class PaymentLessonListView(generics.ListAPIView):  # Lesson
    serializer_class = PaymentLessonSerializer
    queryset = Payment.objects.all()


class PaymentLessonCreatAPIView(generics.CreateAPIView):
    serializer_class = PaymentLessonSerializer


class PaymentCourseListView(generics.ListAPIView):  # Course
    serializer_class = PaymentCourseSerializer
    queryset = Payment.objects.all()


class PaymentCourseCreatAPIView(generics.CreateAPIView):
    serializer_class = PaymentCourseSerializer