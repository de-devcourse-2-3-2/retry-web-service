from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from .views import *

# static file url example :
# www.example.com:8000/static/media/image01.png

urlpatterns = [
    path('', index, name='index'),
    path('chart', chart, name='chart'),
]