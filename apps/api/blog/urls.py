from rest_framework.routers import DefaultRouter

from apps.api.blog.views import ArticleViewSer

urlpatterns = []

router = DefaultRouter()
router.register('article', ArticleViewSer, basename='article')

urlpatterns += router.urls

