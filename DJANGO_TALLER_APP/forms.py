from django import forms
from wsgiref.validate import validator
from django.core import validators

from .models import Reservas


class FormReservas(forms.Form):
    ESTADOS = [('Reservado', 'RESERVADO'), ('Completada', 'COMPLETADA'),
               ('Anulada', 'ANULADA'), ('No asisten', 'NO ASISTEN')]

    nombreResponsable = forms.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(15)
    ])
    telefono = forms.CharField()
    fechaReserva = forms.DateField()
    horaReserva = forms.CharField()
    telefono = forms.CharField()
    cantidad = forms.IntegerField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(15)
    ])
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    observacion = forms.CharField(required=False)

    nombreResponsable.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fechaReserva.widget.attrs['class'] = 'form-control'
    horaReserva.widget.attrs['class'] = 'form-control'
    cantidad.widget.attrs['class'] = 'form-control'
    cantidad.widget.attrs['min'] = '0'
    estado.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'

    nombreResponsable.label = "Nombre Responsable"
    fechaReserva.label = "Fecha Reserva"
    horaReserva.label = "Hora Reserva"
    observacion.label = "Observación"
    telefono.label = "Teléfono"

class FormReservas(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'
    
    ESTADOS = [('Reservado', 'RESERVADO'), ('Completada', 'COMPLETADA'),
               ('Anulada', 'ANULADA'), ('No asisten', 'NO ASISTEN')]

    nombreResponsable = forms.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(15)
    ])
    telefono = forms.CharField()
    fechaReserva = forms.DateField()
    horaReserva = forms.CharField()
    telefono = forms.CharField()
    cantidad = forms.IntegerField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(15)
    ])
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    observacion = forms.CharField(required=False)

    nombreResponsable.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fechaReserva.widget.attrs['class'] = 'form-control'
    horaReserva.widget.attrs['class'] = 'form-control'
    cantidad.widget.attrs['class'] = 'form-control'
    cantidad.widget.attrs['min'] = '0'
    estado.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'

    nombreResponsable.label = "Nombre Responsable"
    fechaReserva.label = "Fecha Reserva"
    horaReserva.label = "Hora Reserva"
    observacion.label = "Observación"
    telefono.label = "Teléfono"
