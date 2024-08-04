from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TutorRequest
from .serializers import TutorRequestSerializer

from rest_framework import generics

class TutorRequestCreateView(generics.CreateAPIView):
    queryset = TutorRequest.objects.all()
    serializer_class = TutorRequestSerializer



