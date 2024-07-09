from django.contrib import admin
from . models import Profile, Otp

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = (
        'user',
        'phone',
    )

@admin.register(Otp)
class Otp(admin.ModelAdmin):
    list_display = (
        'email',
        'otp',
        'valid_til',
        'count',
        'utilized',
        'created_at',
    )