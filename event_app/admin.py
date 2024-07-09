from django.contrib import admin
from . models import VisitorMessage

@admin.register(VisitorMessage)
class VisitorMessage(admin.ModelAdmin):
    list_display = (
        'email',
        'message',
        'read',
        'created_at',
    )
