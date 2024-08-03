from django.contrib import admin
from .models import TutorRequest

@admin.register(TutorRequest)
class TutorRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'board', 'grade', 'subject', 'created_at']
    search_fields = ['name', 'email', 'phone']
