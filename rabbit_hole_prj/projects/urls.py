from django.urls import path, include
from projects import views

urlpatterns = [
    path('', views.projects_list),
    path('<int:pk>/', views.project_detail),
]