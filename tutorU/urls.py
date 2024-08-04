from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tutor-request/', views.tutor_request, name='tutor_request'),
    # Add other paths as needed
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
