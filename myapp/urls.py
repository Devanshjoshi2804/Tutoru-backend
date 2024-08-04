from django.urls import path
from . import views

urlpatterns = [
    path('tutor-request/', views.tutor_request, name='tutor_request'),
    # Add other paths as needed
]
