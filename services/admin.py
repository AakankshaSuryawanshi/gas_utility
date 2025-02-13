from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'request_type', 'status', 'created_at')  # Use correct field names

admin.site.register(ServiceRequest, ServiceRequestAdmin)
