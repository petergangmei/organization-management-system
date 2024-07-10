from django.db import models
from django.utils.text import slugify

class VisitorMessage(models.Model):
    email          =   models.CharField(max_length=100)
    message        =   models.TextField()
    read           =   models.BooleanField(default=False)       
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.email
    
class NewsModel(models.Model):
      title             = models.CharField(max_length=100)
      slug              = models.SlugField(unique=True, blank=True,null=True)
      cover_img         = models.ImageField(upload_to="news-cover-image/",blank=True,null=True)           


      content           = models.TextField()

      public            = models.BooleanField(default=True)

      updated_at = models.DateTimeField(auto_now=True)
      created_at = models.DateTimeField(auto_now_add=True)

      def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

      def __str__(self):
           return self.title