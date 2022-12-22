"""
plugin URL Configuration
"""

from django.urls import path

from api.views import EnvAPIView

urlpatterns = [
    path('api/v1/env', EnvAPIView.as_view()),
]
