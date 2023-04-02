from urllib.parse import urlparse

from rest_framework import serializers


class LinkVideoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = urlparse(value.get('link_to_video')).netloc
        if link not in ['youtube.com']:
            raise serializers.ValidationError('Link to unauthorized source')
