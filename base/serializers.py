from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):

    short_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Link
        fields = ['code', 'url', 'short_url']

    def get_short_url(self, obj):
        return obj.short_url
