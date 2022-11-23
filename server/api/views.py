from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *


class EntidadViewSet(viewsets.ModelViewSet):
    queryset = EstatusEntidad.objects.all()
    serializer_class = EntidadSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.filter(estatus=1)
    serializer_class = ProyectoSerializer

    def destroy(self, request, *args, **kwargs):
        proyect = self.get_object()
        proyect.estatus_id = 2
        proyect.save()
        return Response(data="Proyecto eliminado.")


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.filter(estatus=1)
    serializer_class = AreaSerializer

    def destroy(self, request, *args, **kwargs):
        area = self.get_object()
        area.estatus_id = 2
        area.save()
        return Response(data="Area eliminada.")


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(estatus=1)
    serializer_class = UsuarioSerializer

    def destroy(self, request, *args, **kwargs):
        usuario = self.get_object()
        usuario.estatus_id = 2
        usuario.save()
        return Response(data="Usuario eliminado.")


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def destroy(self, request, *args, **kwargs):
        ticket = self.get_object()
        ticket.estatus_id = 2
        ticket.save()
        return Response(data="Usuario eliminado.")
