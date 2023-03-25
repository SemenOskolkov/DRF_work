from django.core.management import BaseCommand

from financial_accounting.models import Payment
from study.models import Course, Lesson
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment = [
            {
                'user': User.objects.filter(pk=1).first(),
                'paid_course': Course.objects.filter(pk=1).first(),
                'payment_amount': 200000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=2).first(),
                'paid_course': Course.objects.filter(pk=1).first(),
                'payment_amount': 200000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=3).first(),
                'paid_course': Course.objects.filter(pk=2).first(),
                'payment_amount': 160000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=4).first(),
                'paid_course': Course.objects.filter(pk=3).first(),
                'payment_amount': 100000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=5).first(),
                'paid_course': Lesson.objects.filter(pk=1).first(),
                'payment_amount': 80000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=6).first(),
                'paid_course': Lesson.objects.filter(pk=1).first(),
                'payment_amount': 35000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=7).first(),
                'paid_course': Lesson.objects.filter(pk=5).first(),
                'payment_amount': 35000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=8).first(),
                'paid_course': Lesson.objects.filter(pk=2).first(),
                'payment_amount': 12000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=8).first(),
                'paid_course': Lesson.objects.filter(pk=4).first(),
                'payment_amount': 20000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=8).first(),
                'paid_course': Lesson.objects.filter(pk=7).first(),
                'payment_amount': 15000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
            {
                'user': User.objects.filter(pk=9).first(),
                'paid_course': Lesson.objects.filter(pk=10).first(),
                'payment_amount': 10000.0,
                'payment_method': Payment.METHOD_TRANSFER
            },
        ]

        payment_list = []
        Payment.objects.all().delete()

        for item in payment:
            payment_list.append(Payment(**item))

        Payment.objects.bulk_create(payment_list)
