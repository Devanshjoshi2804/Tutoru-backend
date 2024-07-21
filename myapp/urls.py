from django.urls import path
from .views import TutorRequestView

urlpatterns = [
    path('api/tutor-request/', TutorRequestView.as_view(), name='tutor-request'),
]
