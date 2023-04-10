from rest_framework import viewsets, generics

from study.models import Course, Lesson
from study.permissions import SuperUserPerms, ModeratorPerms, OwnerPerms
from study.serializers.course import CourseSerializer, CourseListSerializer, CourseDetailSerializer
from study.serializers.lesson import LessonListSerializer, LessonSerializer, LessonDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializers = {
        'list': CourseListSerializer,
        'retrieve': CourseDetailSerializer,
    }
    permission_classes = [SuperUserPerms | ModeratorPerms | OwnerPerms]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perms(['study.change_course', 'study.view_course']):
            return queryset
        return queryset.filter(owner=self.request.user)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()
    permission_classes = [SuperUserPerms | ModeratorPerms | OwnerPerms]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perms(['study.change_lesson', 'study.view_lesson']):
            return queryset
        return queryset.filter(owner=self.request.user)


class LessonCreatAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()
    permission_classes = [SuperUserPerms | ModeratorPerms | OwnerPerms]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [SuperUserPerms | ModeratorPerms | OwnerPerms]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [SuperUserPerms | ModeratorPerms | OwnerPerms]
