from django.urls import path
from . import views
urlpatterns = [
    path('article/<article_id>/', views.get_article, name='get_article'),
    path('article_new/', views.create_post, name='create_post'),
    path('articles/', views.archive, name='archive'),
    path('', views.archive, name='archive'),
]
