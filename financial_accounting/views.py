import requests
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from financial_accounting.models import Payment
from financial_accounting.serializers import PaymentCourseSerializer, PaymentLessonSerializer
from study.models import Course


class PaymentLessonListView(generics.ListAPIView):  # Lesson
    serializer_class = PaymentLessonSerializer
    queryset = Payment.objects.all()


class PaymentLessonCreatAPIView(generics.CreateAPIView):
    serializer_class = PaymentLessonSerializer


class PaymentCourseListView(generics.ListAPIView):  # Course
    serializer_class = PaymentCourseSerializer
    queryset = Payment.objects.all()


class PaymentCourseCreatAPIView(generics.CreateAPIView):
    serializer_class = PaymentCourseSerializer


class PayCourseAPIView(APIView):

    def get(self, *args, **kwargs):
        course_pk = self.kwargs.get('pk')
        course_item = get_object_or_404(Course, pk=course_pk)
        user = self.request.user

        pay_object = Payment.objects.create(payment_amount=course_item.price, payment_method=Payment.METHOD_TRANSFER,
                                            paid_course=course_item, user=user)

        data_for_request = {
            "TerminalKey": settings.TERMINAL_KEY,
            "Amount": course_item.price,
            "OrderId": pay_object.pk,
            "DATA": {
                "Email": user.email
            },
            "Receipt": {
                "Email": user.email,
                "Taxation": "osn",
                "Items": [
                    {
                        "Name": course_item.name,
                        "Price": course_item.price,
                        "Quantity": 1.00,
                        "Amount": course_item.price,
                        "PaymentObject": "service",
                        "Tax": "vat20"
                    }
                ]
            }
        }

        request = requests.post('https://securepay.tinkoff.ru/v2/Init/', json=data_for_request)

        if request.json()["Success"] == True:
            pay_object.link_pay = request.json()["PaymentURL"]
            pay_object.save()

        return Response({"link_pay": request.json()["PaymentURL"], "data": request.json()})