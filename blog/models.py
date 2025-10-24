from django.db import models
from django.utils import timezone

# Create your models here.

class BlogPost(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"BlogPost {self.id} - {self.content[:50]}"
