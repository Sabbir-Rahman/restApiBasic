from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet, GenericArticleViewset, ModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('articleGeneric', GenericArticleViewset, basename='articleGeneric')
router.register('articleModel', GenericArticleViewset, basename='articleModel')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('articles/', article_list),
    path('classBasedArticles/',ArticleAPIView.as_view()),
    path('detail/<int:pk>/', article_detail),
    path('classBasedDetails/<int:id>/',ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    
   
]
