from django.contrib import admin

from financial_accounting.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'paid_course', 'paid_lesson', 'date_payment', 'payment_amount', 'payment_method',)