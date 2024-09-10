from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailsView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
)

urlpatterns = [
    path("<int:pk>/", ArticleDetailsView.as_view(), name='article_details'),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name='article_edit'),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name='article_delete'),
    path("new/" , ArticleCreateView.as_view(), name="article_new"),
    path('', ArticleListView.as_view(), name='article_list'),
]