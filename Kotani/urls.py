# project/urls.py

from django.contrib import admin
from django.urls import path
from .api import api_v1

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/', include('Gusto.v1_api_urls')),  # Ensure this is the correct path to your app's api_urls
    path("api/v1/", api_v1.urls)
]