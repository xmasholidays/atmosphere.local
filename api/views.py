from django.views.decorators.cache import never_cache

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Audio, Request
from .serializers import AudioSerializer, RequestSerializer
from .permissions import IsLocalhostRequest

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    @never_cache
    @list_route(methods=['get'], permission_classes=[IsLocalhostRequest])
    def next(self, request):
        top_request = Request.objects.all()[0]
        serializer = RequestSerializer(top_request)
        return Response(serializer.data)


class AudioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
