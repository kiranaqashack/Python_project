from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateAPI

urlpatterns = [
    url(r'^createapi/$', CreateAPI.as_view(), name="Create API Data"),
]

