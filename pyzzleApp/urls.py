from django.urls import path
from . import views

urlpatterns = [
    path('run_bfs/', views.run_bfs, name='run_bfs'),
    path('run_best_first_search/', views.run_best_first_search, name='run_best_first_search'),
    path('run_a_star/', views.run_a_star, name='run_a_star'),
]
