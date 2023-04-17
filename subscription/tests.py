from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Course
from subscription.models import Subscription
from users.models import User


class SubscribeTestCase(APITestCase):
    email = 'user10@test.ru'
    password = '12ddfs984dsa'
    first_name = 'User'
    last_name = 'Ten'

    def setUp(self) -> None:

        self.course = Course.objects.create(
            name='Test: Курс 1',
            description='Test: Информация по курсу 1',
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

    def _send_subscription_request(self):
        self.client.post('/subscription/',
                         {
                             "course": self.course.pk,
                         }
                         )

    def test_subscription_create(self):
        queryset = Subscription.objects.filter(user=self.user, course=self.course)

        self._send_subscription_request()  # Запрос на создание подписки
        self.assertTrue(queryset.exists())

        self._send_subscription_request()  # Запрос на удаление подписки
        self.assertFalse(queryset.exists())
