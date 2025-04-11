from rest_framework import serializers
from .models import Feedback, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class FeedbackSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), source='city', write_only=True
    )

    class Meta:
        model = Feedback
        fields = ['id', 'name', 'phone', 'message', 'created_at', 'reply', 'replied', 'city', 'city_id']
        read_only_fields = ['id', 'created_at', 'reply', 'replied', 'city']


