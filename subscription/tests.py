from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class SubscribeTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(
            email='user10@test.ru',
            first_name='User',
            last_name='Ten',
        )
        self.user.set_password('12ddfs984dsa')
        self.user.is_superuser = True
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
        self.test_course_name = 'Курс 1'
        self.test_course_description = 'Информация по курсу 1'

    def test_subscribe_create(self):
        self.client.post('/study/course/',
                         {
                            "name": self.test_course_name,
                            "description": self.test_course_description,
                            "lessons": [],
                            "owner": []
                         }
                         )

        response = self.client.post('/subscribe/create/',
                                    {
                                        "course": self.test_course_name,
                                        "owner": self.user
                                    }
                                    )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_subscribe_destroy(self):
        self.test_subscribe_create()
        response = self.client.delete('/subscribe/delete/2/',
                                      {
                                          "course": self.test_course_name,
                                          "owner": self.user
                                      })

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT)