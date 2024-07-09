from django.http import JsonResponse
from django.contrib.auth.models import User


def check_email_availability(request,email):
    try:
        User.objects.get(email=email)
        return JsonResponse({'exist':True, 'slug':email})
    except User.DoesNotExist:
        return JsonResponse({'exist':False, 'slug':email})