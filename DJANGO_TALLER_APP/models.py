from django.db import models

class Reservas(models.Model):
    fechaReserva = models.DateField()
    horaReserva = models.CharField(max_length=6)
    nombreResponsable = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.nombreResponsable
