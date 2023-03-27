from django.contrib import admin

from study.models import Lesson, Course


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'description', 'link_to_video',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'description',)