from difflib import restore
from django.shortcuts import render, redirect
from DJANGO_TALLER_APP.forms import FormReservas
from DJANGO_TALLER_APP.models import Reservas


""" Import para apis """
from .serializers import ReservasSelializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request, 'index.html')


def listadoReservas(request):
    reservas = Reservas.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)


def agregarReserva(request):
    form = FormReservas()
    if (request.method == 'POST'):
        form = FormReservas(request.POST)
        if (form.is_valid()):
            """ Rescatar los datos para almacenar en la BD """
            rv = form.cleaned_data
            reserva = Reservas(
                nombreResponsable=rv['nombreResponsable'],
                fechaReserva=rv['fechaReserva'],
                horaReserva=rv['horaReserva'],
                telefono=rv['telefono'],
                cantidad=rv['cantidad'],
                estado=rv['estado'],
                observacion=rv['observacion']
            )
            print("Validos")
            reserva.save()
            """ Evitar que al refrescar ingrese el mismo dato denuevo """
            form = ''
            return redirect('/reservas')

    data = {'form': form, 'titulo': 'Agregar Reserva'}
    return render(request, 'agregar.html', data)


def eliminarReserva(request, id):
    reserva = Reservas.objects.get(id=id)
    reserva.delete()
    return redirect('/reservas')


def actualizarReserva(request, id):
    reserva = Reservas.objects.get(id=id)
    form = FormReservas(instance=reserva)

    if (request.method == 'POST'):
        form = FormReservas(request.POST, instance=reserva)
        if (form.is_valid()):
            form.save()
        return redirect('/reservas')

    data = {'form': form, 'titulo': 'Actualizar proyecto'}
    return render(request, 'agregar.html', data)


""" Creación de las vistas de la API """


@api_view(['GET', 'POST'])
def reservas_list(request):

    if request.method == 'GET':
        reservas = Reservas.objects.all()
        rer = ReservasSelializer(reservas, many=True)
        return Response(rer.data)

    if request.method == 'POST':
        rer = ReservasSelializer(data=request.data)
        if rer.is_valid():
            rer.save()
            return Response(rer.data, status=status.HTTP_201_CREATED)
        return Response(rer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def reservas_detail(request, id):
    try:
        print("aca")
        reserva = Reservas.objects.get(id=id)
        print("pasoo")
    except:
        print("error")
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        rer = ReservasSelializer(reserva)
        return Response(rer.data)

    if request.method == 'PUT':
        rer = ReservasSelializer(reserva, data=request.data)
        if rer.is_valid():
            rer.save()
            return Response(rer.data)
        return Response(rer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)