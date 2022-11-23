from rest_framework import serializers
from .models import *
from django.db import models


class EntidadSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = EstatusEntidad
        fields = "__all__"


class ProyectoSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = Proyecto
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = Area
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = Usuario
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = Ticket
        fields = "__all__"
