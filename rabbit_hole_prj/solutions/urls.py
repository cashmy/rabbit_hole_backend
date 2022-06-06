from django.urls import path, include
from solutions import views

urlpatterns = [
    path('', views.solutions_all_list),                                  # Get all solutions 
    path('<int:pk>/', views.solution_detail),                        # Get, update, delete solution
    path('rabbit_hole/<int:rabbit_hole_id>/', views.solutions_list), # Get/Create solutions by rabbit_hole
]