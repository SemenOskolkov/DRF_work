from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User(
            email='user10@test.ru',
            first_name='User',
            last_name='Ten',
        )
        self.user.set_password('12ddfs984dsa')
        self.user.save()

        response = self.client.post(
            '/users/token/',
            {
                "email": 'user10@test.ru',
                "password": "12ddfs984dsa"
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
        self.test_lesson_create()
        response = self.client.get('/study/lesson/12/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'name': self.test_lesson_name,
                'preview': None,
                'description': self.test_lesson_description,
                'link_to_video': self.test_lesson_link_to_video,
            }
        )

    def test_lesson_update(self):  #
        self.test_lesson_create()
        response = self.client.put('/study/lesson/update/12/',
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
                'name': self.test_lesson_new_name,
                'preview': None,
                'description': self.test_lesson_new_description,
                'link_to_video': self.test_lesson_new_link_to_video,
            }
        )

    def test_lesson_delete(self):  #
        self.test_lesson_create()
        response = self.client.delete('/study/lesson/delete/12/')

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
