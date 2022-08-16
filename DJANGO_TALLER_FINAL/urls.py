from django.contrib import admin
from django.urls import path

""" Importar vistas """
from DJANGO_TALLER_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('reservas/', views.listadoReservas),
    path('agregar/', views.agregarReserva),
    path('eliminar/<int:id>', views.eliminarReserva),
    path('actualizar/<int:id>', views.actualizarReserva),
    path('api/reservas/', views.reservas_list),
    path('api/reservas/<int:id>', views.reservas_detail)
]
