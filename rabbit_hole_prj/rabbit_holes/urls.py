from django.urls import path, include
from rabbit_holes import views

urlpatterns = [
    path('', views.rabbit_holes_all_list),                      # Get all rabbit_holes
    path('<int:pk>/', views.rabbit_hole_detail),                # Get, update, delete rabbit_hole
    path('project/<int:project_id>/', views.rabbit_holes_list), # Get/Create rabbit_holes by project
]