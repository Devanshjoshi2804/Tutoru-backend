from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/api/', include('myapp.urls')),  # This should point to your app's URL configuration
]
