from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer


class ArticleList(APIView):
      def get(self, request):
            published_articles = Article.objects.filter(status=Article.Status.PUBLISHED)
            serializer = ArticleSerializer(published_articles, many=True)
            return Response(serializer.data)
      
      def post(self, request):
            serializer = ArticleSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print(serializer.validated_data)
            return Response('OK')