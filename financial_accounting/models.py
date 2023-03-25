from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    METHOD_CASH = 'cash'
    METHOD_TRANSFER = 'transfer_to_account'

    METHODS = (
        ('cash', 'наличные'),
        ('transfer_to_account', 'перевод на счет'),
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    paid_course = models.ForeignKey('study.Course', on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey('study.Lesson', on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный урок')

    date_payment = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    payment_amount = models.FloatField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=50, choices=METHODS, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.payment_amount} {self.date_payment}'
    