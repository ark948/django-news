from django.urls import path
from articles import views

urlpatterns = [
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", views.ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", views.ArticleDeleteView.as_view(), name="article_delete"),
    path("new/", views.ArticleCreateView.as_view(), name="article_new"),
    path("", views.ArticleListView.as_view(), name="article_list"),
]