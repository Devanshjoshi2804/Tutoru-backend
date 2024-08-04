from django.urls import path
from .views import TutorRequestCreateView
from . import views

urlpatterns = [
    path('api/tutor-request/', TutorRequestCreateView.as_view(), name='tutor-request'),
    path('tutor-request/', views.tutor_request, name='tutor_request'),
    # Add other paths as needed
]
