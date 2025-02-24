from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user            =   models.ForeignKey(User,on_delete=models.CASCADE)
    phone           =   models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Designation(models.Model):
        role        =   models.CharField(max_length=100)        

        updated_at  = models.DateTimeField(auto_now=True)
        created_at  = models.DateTimeField(auto_now_add=True)

        def __str__(self):
              return self.role


class Leadership(models.Model):
        name        = models.CharField(max_length=100)
        img         = models.ImageField(upload_to="leadership_img")
        designation = models.ForeignKey(Designation,on_delete=models.DO_NOTHING)
        
        tenure_start= models.DateField(blank=True,null=True)
        tenure_end  = models.DateField(blank=True,null=True)


        updated_at  = models.DateTimeField(auto_now=True)
        created_at  = models.DateTimeField(auto_now_add=True)

        def __str__(self):
              return self.name

class Otp(models.Model):
        email       = models.CharField(max_length=100, blank=True,null=True)
        otp         = models.IntegerField(default=0)
        valid_til   = models.DateTimeField(blank=True,null=True)
        count       = models.IntegerField(default=0)
        token       = models.CharField(max_length=250)
        
        motive      = models.CharField(max_length=100,blank=True,null=True)
        utilized    = models.BooleanField(default=False)

        updated_at  = models.DateTimeField(auto_now=True)
        created_at  = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.email
        
