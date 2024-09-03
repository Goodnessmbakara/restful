from rest_framework import viewsets,permissions
from .models import Article
from .serializers import ArticleSerializer



class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny,)
    
    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)