from django.contrib import admin

from .models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
      list_display = ['id', 'title', 'body', 'author']
      prepopulated_fields = {'slug': ('title',)}

# Register your models here.
