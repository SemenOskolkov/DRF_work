from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User(email='admin@testsite.com')
        self.user.set_password('djangoadmin')
        self.user.save()

        response = self.client.post(
            '/users/token/',
            {"email": 'admin@testsite.com', "password": "djangoadmin"}
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_lesson_create(self):
        response = self.client.post('study/lesson/create/',
                                    {'name': 'Урок 1',
                                     'description': 'Информация по уроку 1',
                                     'link_to_video': 'https://www.youtube.com/1223W2'}
                                    )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_lesson_retrieve(self):
        self.test_lesson_create()
        response = self.client.get('study/lesson/12/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{
                'name': 'Урок 1',
                'preview': None,
                'description': 'Информация по уроку 1',
                'link_to_video': 'https://www.youtube.com/1223W2',
                'owner': 1
            }]
        )

    def test_lesson_update(self):
        self.test_lesson_create()

        response = self.client.put('study/lesson/update/12/',
                                   {'name': 'Урок первый',
                                    'description': 'Информация по первому уроку',
                                    'link_to_video': 'https://www.youtube.com/1223W2'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'name': 'Урок первый',
                'preview': None,
                'description': 'Информация по первому уроку',
                'link_to_video': 'https://www.youtube.com/1223W2',
                'owner': 1
            }
        )

    def test_lesson_delete(self):
        self.test_lesson_create()
        response = self.client.delete('study/lesson/delete/12/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
