# myapp/admin.py

from django.contrib import admin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import TutorRequest

def export_as_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="tutor_requests.pdf"'

    p = canvas.Canvas(response)
    y = 800
    for obj in queryset:
        p.drawString(100, y, f"Name: {obj.name}, Email: {obj.email}, Phone: {obj.phone}, Board: {obj.board}, Grade: {obj.grade}, Subject: {obj.subject}, Created at: {obj.created_at}")
        y -= 20
    p.showPage()
    p.save()
    return response

export_as_pdf.short_description = "Export selected items to PDF"

@admin.register(TutorRequest)
class TutorRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'board', 'grade', 'subject', 'created_at']
    search_fields = ['name', 'email', 'phone']
    actions = [export_as_pdf]

# Ensure static files are being served correctly
admin.site.site_header = "TutorU Admin"
admin.site.site_title = "TutorU Admin Portal"
admin.site.index_title = "Welcome to TutorU Admin Portal"
