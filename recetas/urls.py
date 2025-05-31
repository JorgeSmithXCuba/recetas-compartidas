from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_recetas, name='listar_recetas'),
    path('receta/<int:pk>/', views.mostrar_receta, name='mostrar_receta'),
    path('receta/agregar/', views.agregar_receta, name='agregar_receta'),
    path('categoria/<str:categoria>/', views.listar_recetas_por_categoria, name='listar_recetas_por_categoria'),
    path('buscar/', views.buscar_recetas, name='buscar_recetas'),
]
