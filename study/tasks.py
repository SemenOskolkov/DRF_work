from datetime import datetime

import pytz
from celery import shared_task
from django.core.mail import send_mail

from config import settings
from study.models import Course
from subscription.models import Subscription


@shared_task
def send_course_update(course_pk):
    course_item = Course.objects.filter(pk=course_pk).first()
    subscription_item = Subscription.objects.filter(course=course_pk)
    time = datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE))  # Устанавливаем время NOW в тайм-зоне проекта

    if time >= course_item.datetime_update:

        for owner in subscription_item:
            send_mail(
                subject=f'Обновление курса {course_item.name}',
                message=f'Для просмотра изменений в курсе перейдите по ссылке {settings.BASE_DIR}course/{course_pk}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[owner.owner.email],
                fail_silently=False
            )
