from django.urls import path
from .views import FeedbackAPIView, CityListAPIView

urlpatterns = [
    path('feedback/', FeedbackAPIView.as_view(), name='feedback'),
    path('cities/', CityListAPIView.as_view(), name='city-list'),
]