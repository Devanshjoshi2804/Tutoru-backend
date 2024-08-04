from django.urls import path
from .views import TutorRequestCreateView

urlpatterns = [
    path('api/tutor-request/', TutorRequestCreateView.as_view(), name='tutor_request'),
]
