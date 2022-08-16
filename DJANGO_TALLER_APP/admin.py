from django.contrib import admin

from DJANGO_TALLER_APP.models import Reservas

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id','nombreResponsable','fechaReserva','horaReserva','cantidad','estado']

admin.site.register(Reservas, ReservaAdmin)