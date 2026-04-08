from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=200)  
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title