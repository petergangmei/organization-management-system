
import jwt
from django_thread import Thread
from django.utils import timezone
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from django.conf import settings
from core.utils.calculator import get_datetime_from_timestamp
from core.utils.services import update_otp
from baseapp.models import Otp


def send_email(data):
        subject = data['subject']
        body_text = ''
        body_html = data['body']
        to_email = data['email']

        class send_email_thread(Thread):
            def run(self):
                # from_email = settings.EMAIL_HOST_USER
                from_email = "no-reply@ruangmei.com"
                recipient_list = [to_email]
                email = EmailMultiAlternatives(subject, body_text, from_email, recipient_list)
                email.attach_alternative(body_html, "text/html")
                email.send()
                print('email sent')
        thread = send_email_thread()
        thread.start()
        return JsonResponse({'success':True})


def send_account_opening_otp(token):
    payload = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
    uid = payload['uid']
    otp = payload['otp']
    exp = payload['exp']
    
    mail_subject = "OTP to create your Ruangmei.com account"
    link_address = settings.BASE_URL+"reset-password/?token="+token
    mail_body = render_to_string('emails/register_with_otp.html', {'otp': otp})
    data ={
        'subject':mail_subject,
        'body':mail_body,
        'email':uid
    }
   
    update_otp(token)
    send_email(data)
    return JsonResponse({'success':True})


def contruct_loginotp_email(token):
    payload = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
    uemail = payload['uid']
    otp = payload['otp']
    exp = payload['exp']
    
    mail_subject = "OTP to login into your Ruangmei.com account"
    link_address = settings.BASE_URL+"reset-password/?token="+token
    mail_body = render_to_string('emails/login_with_otp.html', {'otp': otp})
    data ={
        'subject':mail_subject,
        'body':mail_body,
        'email':uemail
    }
    try:
        otpv = Otp.objects.get(email=uemail, valid_til__gt = timezone.now(),utilized=False)
        otpv.otp = otp
        otpv.valid_til =get_datetime_from_timestamp(exp)
        otpv.save()
    except Otp.DoesNotExist:
        Otp.objects.create(email=uemail, otp=otp, valid_til=get_datetime_from_timestamp(exp), token=token)

    send_email(data)
    return JsonResponse({'success':True})


def construct_password_reset_email(token):
    print('jwt scret key: ', settings.JWT_SECRET_KEY)
    payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
    uemail = payload['uid']
    otp = payload['otp']
    exp = payload['exp']

    mail_subject = "Password Reset Email"
    link_address = settings.BASE_URL+"reset-password-token/?token="+token
    mail_body = render_to_string('emails/password_reset.html', {'link': link_address})
    data ={
        'subject':mail_subject,
        'body':mail_body,
        'email':uemail
    }
    try:
        otpv = Otp.objects.get(email=uemail,motive="reset-password", valid_til__gt = timezone.now(),utilized=False)
        otpv.otp = otp
        otpv.valid_til =get_datetime_from_timestamp(exp)
        otpv.save()
    except Otp.DoesNotExist:
        Otp.objects.create(email=uemail, otp=otp, valid_til=get_datetime_from_timestamp(exp), token=token)
    send_email(data)