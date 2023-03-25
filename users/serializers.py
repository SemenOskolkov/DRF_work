from rest_framework import serializers

from financial_accounting.models import Payment
from users.models import User


class PaymentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentUserSerializer(many=True, source='payment_set')

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
