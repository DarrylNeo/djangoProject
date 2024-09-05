from django.urls import path
from .views import image_detection_view

urlpatterns = [
    path('', image_detection_view, name='image_detection'),
]