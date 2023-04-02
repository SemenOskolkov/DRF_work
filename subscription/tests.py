from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class SubscribeTestCase(APITestCase):

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