from django.urls import path
from .api import api_v1

urlpatterns = [
    path('api/v1/', api_v1.urls),
]