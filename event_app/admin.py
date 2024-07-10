from django.contrib import admin
from . models import VisitorMessage, NewsModel

@admin.register(VisitorMessage)
class VisitorMessage(admin.ModelAdmin):
    list_display = (
        'email',
        'message',
        'read',
        'created_at',
    )

@admin.register(NewsModel)
class NewsModel(admin.ModelAdmin):
    list_display = (
        'title',
        'created_at',
    )
