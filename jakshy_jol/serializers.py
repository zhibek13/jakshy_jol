from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ('number_of_news', 'text',)
