from django.urls import path
from .api import api_v3

urlpatterns =[
    path('api/v3/', api_v3.urls)
]
