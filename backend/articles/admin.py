from django.contrib import admin

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
      list_display = ['id', 'title', 'body', 'author', 'published_on', 'status']
      prepopulated_fields = {'slug': ('title',)}

# Register your models here.
