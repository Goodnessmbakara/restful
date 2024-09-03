from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ArticleViewset

router = DefaultRouter()
router.register('', ArticleViewset)

urlpatterns = [
    path('', include(router.urls))
]