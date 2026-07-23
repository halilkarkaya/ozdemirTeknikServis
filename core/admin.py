from django.contrib import admin

from .models import ServiceRequest


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "phone", "device", "handled")
    list_editable = ("handled",)
    list_filter = ("device", "handled")
    search_fields = ("name", "phone")
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
