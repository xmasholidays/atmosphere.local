from .views import RequestViewSet, AudioViewSet

from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'requests', RequestViewSet)
router.register(r'audios', AudioViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]