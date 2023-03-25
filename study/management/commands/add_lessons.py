from django.core.management import BaseCommand

from study.models import Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):
        lesson = [
            {
                'name': 'Основы синтаксиса в Python',
                'description': 'Этот урок объяснит как строится синтаксис программирования на языке Python.',
                'link_to_video': 'http://link_course1/lesson1/'
            },
            {
                'name': 'Классы и база данных',
                'description': 'Этот урок объяснит как работать с Классами и покажет основные команды по работе с БД.',
                'link_to_video': 'http://link_course1/lesson2/'
            },
            {
                'name': 'Django',
                'description': 'Этот урок расскажет как работать в Django.',
                'link_to_video': 'http://link_course1/lesson3/'
            },
            {
                'name': 'Основы системного анализа',
                'description': 'Этот урок объяснит основы системного анализа.',
                'link_to_video': 'http://link_course2/lesson1/'
            },
            {
                'name': 'Построение моделей',
                'description': 'Этот урок расскажет как правильно строить модели.',
                'link_to_video': 'http://link_course2/lesson2/'
            },
            {
                'name': 'Описание бизнес-требований',
                'description': 'Этот урок объяснит как нужно описывать бизнес-требования.',
                'link_to_video': 'http://link_course2/lesson2/'
            },
            {
                'name': 'Основы проектного менеджмента',
                'description': 'Этот урок объяснит основы проектного менеджмента.',
                'link_to_video': 'http://link_course3/lesson1/'
            },
            {
                'name': 'Как рассчитать время на выполнение проекта',
                'description': 'Этот урок объяснит на что нужно обратить внимание при расчете времени проекта.',
                'link_to_video': 'http://link_course3/lesson2/'
            },
            {
                'name': 'MVP',
                'description': 'Этот урок объяснит почему MVP важно для создания проекта.',
                'link_to_video': 'http://link_course3/lesson3/'
            },
            {
                'name': 'Как найти интересную профессию?',
                'description': 'Этот урок поможет найти профессию мечты и расскажет про основы профессии.',
                'link_to_video': 'http://link_find_your_profession/'
            },
        ]

        lesson_list = []
        Lesson.objects.all().delete()

        for item in lesson:
            lesson_list.append(Lesson(**item))

        Lesson.objects.bulk_create(lesson_list)