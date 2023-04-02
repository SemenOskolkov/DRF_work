from rest_framework import serializers

from financial_accounting.models import Payment
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'city',
        )


class PaymentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            'paid_course',
            'paid_lesson',
            'date_payment',
            'payment_amount',
            'payment_method',
        )


class UserProfileInfoSerializer(serializers.ModelSerializer):
    payment = PaymentInfoSerializer(many=True, source='payment_set')

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'city',
            'payment',
        )
