from django.contrib import admin

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
      list_display = ['id', 'title', 'slug', 'author', 'status', 'published_on']
      list_filter = ['status', 'author', 'published_on']
      search_fields = ['title']
      prepopulated_fields = {'slug': ('title',)}
      date_hierarchy = 'published_on'
      ordering = ['published_on']

# Register your models here.
