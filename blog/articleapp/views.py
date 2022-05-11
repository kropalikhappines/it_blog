from rest_framework.viewsets import ModelViewSet
from .models import Article
from .serializers import ArticleModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    