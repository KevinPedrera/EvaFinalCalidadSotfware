from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestionar_rutinas, name='gestionar_rutinas'),
    path('editar/<int:id>/', views.gestionar_rutinas, name='editar_rutina'),
    path('eliminar/<int:id>/', views.eliminar_rutina, name='eliminar_rutina'),
]