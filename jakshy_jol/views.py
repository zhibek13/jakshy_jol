from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView

from .models import News
from .serializers import NewsSerializer


# class NewsListCreate(ListCreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
