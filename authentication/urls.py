from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('pacient_view_set', PacientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]