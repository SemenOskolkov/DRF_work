from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')

    lessons = models.ManyToManyField('study.Lesson', **NULLABLE, verbose_name='Уроки')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    link_to_video = models.CharField(max_length=250, verbose_name='Ссылка  на видео')

    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return f'{self.name}'
