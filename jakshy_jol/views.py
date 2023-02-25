from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import News
from .serializers import NewsSerializer


class NewsList(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

