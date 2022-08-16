from dataclasses import fields
from rest_framework import serializers
from .models import Reservas

class ReservasSelializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = "__all__" 