from django.urls import path, include
from images import views

urlpatterns = [
    path('<str:file>', views.image_file),
]