
import jwt, uuid ,random,json
from datetime import timedelta
from django.utils import timezone
from core.utils.calculator import get_datetime_from_timestamp
from baseapp.models import Otp



def update_otp(token):
    payload = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
    uid = payload['uid']
    otp = payload['otp']
    exp = payload['exp']

    try:
        otpv = Otp.objects.get(email=uid, valid_til__gt = timezone.now(),utilized=False)
        otpv.otp = otp
        if otpv.count >= 3:
            print('otp request exceed limit')
            return False
        otpv.count = otpv.count +1
        otpv.valid_til =get_datetime_from_timestamp(exp)
        otpv.save()
        print('otp updated')
        return True
    except Otp.DoesNotExist:
        Otp.objects.create(email=uid, otp=otp, valid_til=get_datetime_from_timestamp(exp), token=token)
        print('otp created')
        return True