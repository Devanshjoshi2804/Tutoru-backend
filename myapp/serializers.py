from rest_framework import serializers
from .models import TutorRequest

class TutorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorRequest
        fields = '__all__'
