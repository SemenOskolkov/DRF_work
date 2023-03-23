from django.urls import path

from rest_framework.routers import DefaultRouter
from study.apps import StudyConfig
from study.views import CourseViewSet, LessonListView, LessonCreatAPIView

app_name = StudyConfig.name
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreatAPIView.as_view(), name='lesson_create')
] + router.urls