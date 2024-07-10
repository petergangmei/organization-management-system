from django.contrib import admin
from . models import Profile, Otp, Leadership, Designation

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

@admin.register(Designation)
class Designation(admin.ModelAdmin):
    list_display = (
        'role',
        'created_at',
    )

@admin.register(Leadership)
class Designation(admin.ModelAdmin):
    list_display = (
        'name',
        'designation',
        'tenure_start',
        'tenure_end',
        'created_at',
    )