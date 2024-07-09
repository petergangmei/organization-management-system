from django.db import models

class VisitorMessage(models.Model):
    email          =   models.CharField(max_length=100)
    message        =   models.TextField()
    read           =   models.BooleanField(default=False)       
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.email