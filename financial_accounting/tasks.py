import hashlib

import requests
from celery import shared_task
from rest_framework import status

from config import settings
from financial_accounting.models import Payment


@shared_task
def check_status_pay():
    payment_items = Payment.objects.filter(payment_method=Payment.METHOD_TRANSFER, pay_status=Payment.CREATED)

    for pay_object in payment_items:
        hash_token = hashlib.sha256(
            f"{settings.TINKOFF_TERMINAL_PASSWORD}{pay_object.tinkoff_payment_id}{settings.TINKOFF_TERMINAL_KEY}".encode())
        token = hash_token.hexdigest()

        data_for_request = {
            "TerminalKey": settings.TINKOFF_TERMINAL_KEY,
            "PaymentId": pay_object.tinkoff_payment_id,
            "Token": token
        }

        response = requests.post(
            f'{settings.TINKOFF_URL}GetState', json=data_for_request
        )

        if response.status_code == status.HTTP_200_OK:
            response_json = response.json()

            if response_json.get('CONFIRMED'):
                pay_object.pay_status = Payment.CONFIRMED
                pay_object.save()
            elif response_json.get('REJECTED'):
                pay_object.pay_status = Payment.REJECTED
                pay_object.save()
