from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Subscription(models.Model):
    STATUS_SIGNED = 'signed'
    STATUS_NOT_SIGNED = 'not_signed'

    STATUSES = (
        (STATUS_SIGNED, 'подписан'),
        (STATUS_NOT_SIGNED, 'не подписан')
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    course = models.ForeignKey('study.Course', on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_NOT_SIGNED, verbose_name='статус подписки')

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return f'{self.user} {self.course} {self.status}'