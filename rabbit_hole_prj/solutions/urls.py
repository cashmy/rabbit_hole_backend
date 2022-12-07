from django.urls import path, include
from solutions import views

urlpatterns = [
    path('', views.solution_add),                              # Add POST a solution
    path('<int:pk>/', views.solution_detail),                  # Get, update, delete solution
]