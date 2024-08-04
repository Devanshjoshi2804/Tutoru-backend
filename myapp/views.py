from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TutorRequest
from .serializers import TutorRequestSerializer

from rest_framework import generics
# myapp/views.py
from django.http import JsonResponse

@csrf_exempt
def tutor_request(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Process your data here
            return JsonResponse({'message': 'Request received'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

class TutorRequestCreateView(generics.CreateAPIView):
    queryset = TutorRequest.objects.all()
    serializer_class = TutorRequestSerializer



