from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Subscription(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey('study.Course', on_delete=models.CASCADE, verbose_name='Курс')

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return f'{self.user} {self.course}'