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


class EspecialistaSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = Especialista
        fields = "__all__"


class PrioridadSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = Prioridad
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    objects: models.Manager()
 
    class Meta:
        model = Ticket
        fields = "__all__"


class EstatusSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = EstatusTicket
        fields = "__all__"


class ComentarioSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = Comentario
        fields = "__all__"


class HistorialSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = Historial
        fields = "__all__"


class RolSerializer(serializers.ModelSerializer):
    objects: models.Manager()

    class Meta:
        model = Rol
        fields = "__all__"
