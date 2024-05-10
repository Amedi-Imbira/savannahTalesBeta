from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
      list_display = ['id', 'title', 'slug', 'author', 'published_on', 'status']
      list_filter = ['status', 'published_on', 'author']
      search_fields = ['title', 'author']
      prepopulated_fields = {'slug': ('title',)}
      ordering = ['status', 'published_on']