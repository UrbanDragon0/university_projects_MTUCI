from django.urls import path
from . import views
urlpatterns = [
    path('', views.archive, name='archive'),
    #path(r'^article/(?P<article_id>\d+)$', views.get_article, name='get_article')
    path('article/<article_id>/', views.get_article, name='get_article'),
]
