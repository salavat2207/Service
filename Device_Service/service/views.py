from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

from .models import Feedback
from .serializers import FeedbackSerializer
"""
“Форма обратной связи” через API:
"""
class FeedbackAPIView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            feedback = serializer.save()

            # Email-уведомление на почту администратора
            subject = f"Новое сообщение от {feedback.name}"
            message = f"Email: {feedback.email}\n\nСообщение:\n{feedback.message}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])

            return Response({"message": "Спасибо за обращение!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# def serch(): #реализация поиска на сайте