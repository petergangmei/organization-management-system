
import jwt, uuid ,random,json
from datetime import timedelta
from django.utils import timezone
from django.conf import settings

def generate_username(email):
    unique_id = 'uid-'+email[:3]+str(uuid.uuid4())[:8]
    return unique_id

def generate_token(uid):
    otp =  random.randint(100000, 999999)
    expiration_time = timezone.now() + timedelta(minutes=10)
    print('exprity time ------- ', expiration_time)
    payload = {
        'uid': uid,
        'otp': otp,
        'exp': expiration_time
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
    return token