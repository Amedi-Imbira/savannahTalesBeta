from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Publication
from .serializers import PublicationSerializer

class PublicationList(APIView):
      def get(self, request):
            publications = Publication.objects.all()
            serializer = PublicationSerializer(publications, many=True)
            return Response(serializer.data)
      
      def post(self):
            serializer = PublicationSerializer(data=request.data)
            
# Create your views here.
