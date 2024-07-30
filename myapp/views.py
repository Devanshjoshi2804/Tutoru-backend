import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TutorRequest
from .serializers import TutorRequestSerializer

logger = logging.getLogger(__name__)

class TutorRequestView(APIView):
    def post(self, request):
        logger.info(f"Received data: {request.data}")
        serializer = TutorRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
