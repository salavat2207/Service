from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.core.mail import send_mail
from django.conf import settings

from .models import Feedback, City
from .serializers import FeedbackSerializer, CitySerializer

from .utils import send_telegram_message




#
# """
# “Форма обратной связи” через API на электронную почту:
# """
# class FeedbackAPIView(APIView):
#     def post(self, request):
#         serializer = FeedbackSerializer(data=request.data)
#         if serializer.is_valid():
#             feedback = serializer.save()
#
#             # Email-уведомление на почту администратора
#             subject = f"Новое сообщение от {feedback.name}"
#             message = f"Email: {feedback.email}\n\nСообщение:\n{feedback.message}"
#             send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
#
#             return Response({"message": "Спасибо за обращение!"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

"""
“Список городов” через API:
"""
class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer



"""
“Форма обратной связи” через API через Telegram:
"""


class FeedbackAPIView(generics.CreateAPIView):
    ...

    def perform_create(self, serializer):
        feedback = serializer.save()

        # Email
        ...

        # Telegram
        tg_message = (
            f"<b>Новая заявка</b>\n"
            f"<b>Имя:</b> {feedback.name}\n"
            f"<b>Email:</b> {feedback.email}\n"
            f"<b>Город:</b> {feedback.city.name if feedback.city else 'Не указано'}\n"
            f"<b>Сообщение:</b> {feedback.message}"
        )
        send_telegram_message(tg_message)