import time,jwt
from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import  authenticate, login, logout
from django.utils import timezone
from django.conf import settings
from baseapp.models import Otp
from core.utils.generator import generate_username,generate_token
from core.utils.mails import construct_password_reset_email
from event_app.models import VisitorMessage

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        uid = request.POST.get('email')
        pass2 = request.POST.get('password2')
        user = User.objects.create(username=generate_username(uid), email=uid, password=make_password(pass2))
        login(request, user)
        messages.success(request, "Account Created!")
        return redirect(reverse('baseapp:index'))
    if request.user.is_authenticated:
            return redirect(reverse('baseapp:index'))
    return render(request, 'signup.html')

def login_account(request):
    if request.method == "POST":
         email = request.POST.get('email')
         password = request.POST.get('password1')

         uid = User.objects.get(email=email)
         user = authenticate(username=uid.username, password=password)

         if user is not None:
            messages.success(request, "Account login!")
            login(request, user)
            return redirect(reverse('baseapp:index'))
         messages.error(request, 'Invalid email or password')

    if request.user.is_authenticated:
            return redirect(reverse('baseapp:index'))
    return render(request, 'login.html')

def logout_account(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    
    pass

def forgot_password(request):
     if request.method == 'POST':
        email = request.POST.get('email')
        try:
             User.objects.get(email=email)
             construct_password_reset_email(generate_token(email))
             messages.success(request, 'Password reset link sent to your email.')
             return redirect(reverse('baseapp:forgot-password'))
        except User.DoesNotExist:
             messages.error(request, 'Your email is not registered with us')
             return redirect(reverse('baseapp:forgot-password'))
     if request.user.is_authenticated:
            return redirect(reverse('baseapp:index'))
    
     return render(request, 'password-forgot.html')

def password_reset_token(request):
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        payload = jwt.decode(request.POST.get('token'), settings.JWT_SECRET_KEY, algorithms=['HS256'])
        uid = payload['uid']
        otp = payload['otp']
        
        if pass1 is not None and len(pass1) < 5:
            messages.warning(request, 'Please enter alteast 5 digit password.')
            return redirect(reverse('baseapp:reset-password-token')+"?token="+request.POST.get('token'))

        if pass1 != pass2:
            messages.warning(request, 'You have entered two diffent password.')
            return redirect(reverse('baseapp:reset-password-token')+"?token="+request.POST.get('token'))
        
        user = User.objects.get(email=uid)
        user.password = make_password(pass1)
        user.save()
        pas = Otp.objects.get(email=uid,otp=otp, valid_til__gt=timezone.now(),utilized=False)
        pas.utilized = True
        pas.save()
        messages.success(request, 'Password updated.')
        return redirect(reverse('baseapp:index'))
    else:
        try:
            token = request.GET.get('token')
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            uid = payload['uid']
            otp = payload['otp']
            exp = payload['exp']
            try:
                pas = Otp.objects.get(email=uid, valid_til__gt=timezone.now(),utilized=False)
                if pas.utilized is True:
                    messages.warning(request, 'This token has already been used.')    
                    return redirect(reverse('baseapp:forgot-password'))
                context ={
                    'token':token,
                }
                if request.user.is_authenticated:
                    return redirect(reverse('baseapp:index'))
                return render(request, 'password-reset.html',context)

            except Otp.DoesNotExist:
                # messages.warning(request, 'This token is not valid anymore')
            # Check if OTP is valid and not expired
                return redirect(reverse('baseapp:reset-password'))
        except jwt.ExpiredSignatureError:
            messages.error(request, 'Token has expired')
            return redirect(reverse('baseapp:forgot-password'))
        except jwt.DecodeError:
            messages.warning(request, 'Invalid token')
            return redirect(reverse('baseapp:forgot-password'))
            

def contact_us(request):
     if request.method == "POST":
            email = request.POST.get("email")
            msg   = request.POST.get("message")

            errors = []
            if not email:
                errors.append("Email is required.")
            if not msg:
                errors.append("Message is required.")
            
            if errors:
                for error in errors:
                    messages.error(request, error)
                return redirect(reverse('baseapp:contact-us'))
            
            VisitorMessage.objects.create(email=email,message=msg)
            messages.success(request, "Your message was submited, we will get back to you soon!")
            return redirect(reverse('baseapp:index'))
          

               
     return render(request, 'contact.html')