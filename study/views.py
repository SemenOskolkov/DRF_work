from django.shortcuts import render
from rest_framework import viewsets, generics

from study.models import Course, Lesson
from study.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreatAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
