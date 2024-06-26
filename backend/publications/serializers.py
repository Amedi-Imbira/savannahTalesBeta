from rest_framework import serializers

from .models import Publication

class PublicationSerializer(serializers.ModelSerializer):
      class Meta:
            model = Publication
            fields = ['id', 'title', 'sub_title', 'body', 'author', 'created_at']