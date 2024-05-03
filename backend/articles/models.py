import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
      
      class Status(models.TextChoices):
            DRAFT = 'DF', 'Drafted'
            PUBLISHED = 'PB', 'Published'
            
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      title = models.CharField(max_length=200)
      slug = models.SlugField(max_length=250)
      body = models.TextField()
      status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      published_on = models.DateTimeField(default=timezone.now)
      created_at = models.DateTimeField(auto_now_add=True)
      edited = models.DateTimeField(auto_now=True)
      
      class Meta:
            ordering = ['-published_on']
            indexes = [
                  models.Index(fields=['-published_on']),
            ]
      
      def __str__(self):
            return self.title

# Create your models here.
