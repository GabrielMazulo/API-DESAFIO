from django.urls import path, include
from .api import api_v2

urlpatterns = [
    path('api/v2/', api_v2.urls),
]