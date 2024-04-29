from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleListAPIView.as_view()),
    path("<int:article_id>/", views.ArticleDetailAPIView.as_view()),
    path("<int:article_id>/comments/", views.CommentListAPIView.as_view()),
    path("comments/<int:comment_id>/", views.CommentDetailAPIView.as_view()),
]