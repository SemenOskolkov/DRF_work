from django.core.management import BaseCommand

from study.models import Course, Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):
        course = [
            {
                'name': 'Python',
                'description': 'Этот курс посвящен программированию на языке Python.',
                'lessons': [
                    Lesson.objects.filter(pk=1).first(),
                    Lesson.objects.filter(pk=2).first(),
                    Lesson.objects.filter(pk=3).first(),
                ]
            },
            {
                'name': 'Системный анализ',
                'description': 'Этот курс посвящен системному анализу.',
                'lessons': [
                    Lesson.objects.filter(pk=4).first(),
                    Lesson.objects.filter(pk=5).first(),
                    Lesson.objects.filter(pk=6).first(),
                ]
            },
            {
                'name': 'Менеджмент проектов',
                'description': 'Этот курс посвящен менеджменту проектов.',
                'lessons': [
                    Lesson.objects.filter(pk=7).first(),
                    Lesson.objects.filter(pk=8).first(),
                    Lesson.objects.filter(pk=9).first(),
                ]
            }
        ]

        course_list = []
        Course.objects.all().delete()

        for item in course:
            course_list.append(Course(**item))

        Course.objects.bulk_create(course_list)