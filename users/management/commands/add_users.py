from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users_data = [
            {
                'email': 'user1@site.ru',
                'first_name': 'User',
                'last_name': 'One',
                'phone_number': '+7(999)000-11-11',
                'city': 'Москва',
                'password': '1248dkfdknwjrns'
            },
            {
                'email': 'user2@site.ru',
                'first_name': 'User',
                'last_name': 'Two',
                'phone_number': '+7(999)000-22-22',
                'city': 'Санкт-Петербург',
                'password': 'knsdkfns32421'
            },
            {
                'email': 'user3@site.ru',
                'first_name': 'User',
                'last_name': 'Three',
                'phone_number': '+7(999)000-33-33',
                'city': 'Ростов-на-Дону',
                'password': '3421eksmnsncvsa'
            },
            {
                'email': 'user4@site.ru',
                'first_name': 'User',
                'last_name': 'Four',
                'phone_number': '+7(999)000-44-44',
                'city': 'Новосибирск',
                'password': 'nqeofhj9qfnq25w'
            },
            {
                'email': 'user5@site.ru',
                'first_name': 'User',
                'last_name': 'Five',
                'phone_number': '+7(999)000-55-55',
                'city': 'Москва',
                'password': '93u1rh9fh2nq93'
            },
            {
                'email': 'user6@site.ru',
                'first_name': 'User',
                'last_name': 'Six',
                'phone_number': '+7(999)000-66-66',
                'city': 'Санкт-Петербург',
                'password': '84j23do0wdcnwoqd'
            },
            {
                'email': 'user7@site.ru',
                'first_name': 'User',
                'last_name': 'Seven',
                'phone_number': '+7(999)000-77-77',
                'city': 'Москва',
                'password': '4ewdnwo94hd8w3ds'
            },
            {
                'email': 'user8@site.ru',
                'first_name': 'User',
                'last_name': 'Eight',
                'phone_number': '+7(999)000-88-88',
                'city': 'Челябинск',
                'password': 'rosdcni89472nfo'
            },
            {
                'email': 'user9@site.ru',
                'first_name': 'User',
                'last_name': 'Nine',
                'phone_number': '+7(999)000-99-99',
                'city': 'Самара',
                'password': '94i3irsdkdsaef24'
            },
        ]

        user_list = []

        for item in users_data:
            user_list.append(User(**item))

        User.objects.bulk_create(user_list)