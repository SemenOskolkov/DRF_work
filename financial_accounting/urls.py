from django.urls import path

from financial_accounting.apps import FinancialAccountingConfig
from financial_accounting.views import PaymentLessonListView, PaymentLessonCreatAPIView, PaymentCourseListView, \
    PaymentCourseCreatAPIView, PayCourseAPIView

app_name = FinancialAccountingConfig.name


urlpatterns = [
    path('lesson/list/', PaymentLessonListView.as_view(), name='financial_lesson_list'),
    path('lesson/create/', PaymentLessonCreatAPIView.as_view(), name='financial_lesson_create'),

    path('course/list/', PaymentCourseListView.as_view(), name='financial_course_list'),
    path('course/create/', PaymentCourseCreatAPIView.as_view(), name='financial_course_create'),

    path('pay/<int:pk>/', PayCourseAPIView().as_view(), name='pay_course')
]