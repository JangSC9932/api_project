from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer


# Create your views here.


def article_list_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, "articles/article_list.html", context)


# 커스텀으로 직렬화
def json_01(request):
    articles = Article.objects.all()

    # 리스트에 딕셔너리 형태로 넣기 // JSON 형식의 문자열로 직렬화
    json_articles = []
    for article in articles:
        json_articles.append(
            {
                "title": article.title,
                "content": article.content,
                "created_at": article.created_at,
                "updated_at": article.updated_at,
            }
        )
    # json_articles 가 딕셔너리 형태가 아니기 때문에 safe 는 False로 해줘야 함.
    return JsonResponse(json_articles, safe=False)


# 자동으로 직렬화
def json_02(request):
    articles = Article.objects.all()
    # 자동으로 JSON 형식의 문자열로 직렬화
    res_data = serializers.serialize("json", articles)
    return HttpResponse(res_data, content_type="application/json")


# 자동으로 직렬화 + HTML 생성
@api_view(["GET"])
def json_drf(request):
    articles = Article.objects.all()
    # Article 모델을 이용하여 ArticleSerializer 생성 ( serializers.py )
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)