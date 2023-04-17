from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    email = 'user10@test.ru'
    password = '12ddfs984dsa'
    first_name = 'User'
    last_name = 'Ten'

    def setUp(self) -> None:

        self.lesson = Lesson.objects.create(
            name='Test: Урок 1',
            description='Test: Информация по уроку 1',
            link_to_video='Test: https://youtube.com/1223W2',
        )

        self.user = User.objects.create(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
        )
        self.user.set_password(self.password)
        self.user.is_superuser = True
        self.user.save()

        response = self.client.post(
            '/users/token/',
            {
                "email": self.email,
                "password": self.password
            }
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        '''CREATE Исходные данные'''
        self.test_lesson_name = 'Урок 1'
        self.test_lesson_description = 'Информация по уроку 1'
        self.test_lesson_link_to_video = 'https://youtube.com/1223W2'

        '''UPDATE Новые данные'''
        self.test_lesson_new_name = 'Первый урок'
        self.test_lesson_new_description = 'Информация по первому уроку'
        self.test_lesson_new_link_to_video = 'https://youtube.com/1JHD123'

    def test_lesson_create(self):  # Создание урока
        response = self.client.post('/study/lesson/create/',
                                    {
                                        'name': self.test_lesson_name,
                                        'description': self.test_lesson_description,
                                        'link_to_video': self.test_lesson_link_to_video,
                                     }
                                    )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_lesson(self):  # Просмотр урока
        response = self.client.get(
            reverse('study:lesson_retrieve', args=[self.lesson.pk])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        expected_data = {
            'name': self.lesson.name,
            'preview': None,
            'description': self.lesson.description,
            'link_to_video': self.lesson.link_to_video,
            'owner': None
        }

        self.assertEqual(
            response.json(),
            expected_data
        )

    def test_lesson_update(self):  # Изменение урока
        response = self.client.put(
            reverse('study:lesson_update', args=[self.lesson.pk]),
            {
                'name': self.test_lesson_new_name,
                'description': self.test_lesson_new_description,
                'link_to_video': self.test_lesson_new_link_to_video,
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.pk,
                'name': self.test_lesson_new_name,
                'preview': None,
                'description': self.test_lesson_new_description,
                'link_to_video': self.test_lesson_new_link_to_video,
                'owner': None
            }
        )

    def test_lesson_delete(self):  # Удаление урока
        response = self.client.delete(
            reverse('study:lesson_delete', args=[self.lesson.pk]))

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
