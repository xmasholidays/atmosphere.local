from rest_framework import serializers

from .models import Audio, Request


class RequestSerializer(serializers.ModelSerializer):
    is_background = serializers.BooleanField(source='audio.is_background', read_only=True)
    audio_filepath = serializers.CharField(source='audio.path', read_only=True)
    image_filepath = serializers.CharField(source='audio.image', read_only=True)

    class Meta:
        model = Request
        fields = ('id', 'is_background', 'audio_filepath', 'image_filepath')


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = ('id', 'title', 'is_background')
