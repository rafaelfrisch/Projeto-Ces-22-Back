from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

router = routers.DefaultRouter()
router.register('pacient_view_set', PacientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token),
    path('login/', login)
]