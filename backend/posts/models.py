import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
      class Status(models.TextChoices):
            PUBLISHED = 'PB', 'Published'
            DRAFT = 'DF', 'Drafted'
      
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      title = models.CharField(max_length=200)
      subtitle = models.CharField(max_length=250, blank=True)
      slug = models.SlugField(max_length=250)
      # image = models.ImageField(upload_to='post_images/')
      body = models.TextField()
      status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      published_on = models.DateTimeField(default=timezone.now)
      created_at = models.DateTimeField(auto_now_add=True)
      
      class Meta:
            ordering = ['-published_on']
            indexes = [
                  models.Index(fields=['-published_on'])
            ]
            
      def __str__(self):
            return self.title
      
