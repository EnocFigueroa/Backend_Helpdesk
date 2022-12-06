from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *


class EntidadViewSet(viewsets.ModelViewSet):
    queryset = EstatusEntidad.objects.all()
    serializer_class = EntidadSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.filter(estatus=1)
    serializer_class = ProyectoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'estatus']

    def destroy(self, request, *args, **kwargs):
        proyect = self.get_object()
        proyect.estatus_id = 2
        proyect.save()
        return Response(data="Proyecto eliminado.")


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.filter(estatus=1)
    serializer_class = AreaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

    def destroy(self, request, *args, **kwargs):
        area = self.get_object()
        area.estatus_id = 2
        area.save()
        return Response(data="Area eliminada.")


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(estatus=1)
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

    def destroy(self, request, *args, **kwargs):
        usuario = self.get_object()
        usuario.estatus_id = 2
        usuario.save()
        return Response(data="Usuario eliminado.")


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

    def destroy(self, request, *args, **kwargs):
        ticket = self.get_object()
        ticket.estatus_id = 2
        ticket.save()
        return Response(data="Ticket eliminado.")


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"
