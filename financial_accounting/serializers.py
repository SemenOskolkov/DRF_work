from rest_framework import serializers

from financial_accounting.models import Payment


class PaymentLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            'user',
            'paid_lesson',
            'date_payment',
            'payment_amount',
            'payment_method',
        )


class PaymentCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            'user',
            'paid_course',
            'date_payment',
            'payment_amount',
            'payment_method',
        )
