from rest_framework import serializers

from .models import Publication

class PublicationSerializer(serializers.ModelSerializer):
      model = Publication
      fields = ['id', 'title', 'sub_title', 'body', 'create_at']