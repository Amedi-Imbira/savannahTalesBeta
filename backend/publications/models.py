import uuid
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Publication(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      title = models.CharField(max_length=200)
      sub_title = models.CharField(max_length=200)
      slug = models.SlugField(max_length=250)
      body = models.TextField()
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      caption = models.ImageField(upload_to='uploads/')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      tags = TaggableManager(through=UUIDTaggedItem)
      
      class Meta:
            ordering = ['-created_at']
      
      def __str__(self):
            return self.title