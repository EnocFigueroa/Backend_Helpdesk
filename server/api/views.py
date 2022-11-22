from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


# Vista del modelo Estatus Entidad, que puede ser activo o inactivo
class EntidadView(APIView):
    # Función GET que devuelve todos los objetos
    def get(self, request):
        entidades = EstatusEntidad.objects.all()
        serializer = EntidadSerializer(entidades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Función POST para crear un objeto
    def post(self, request):
        entidad = EntidadSerializer(data=request.data)
        if entidad.is_valid():
            entidad.save()
            return Response(entidad.data, status=status.HTTP_201_CREATED)
        return Response(entidad.errors, status=status.HTTP_400_BAD_REQUEST)


# Vista que devuelve unicamente trabaja con los datos de una instancia
class EntidadDetalle(APIView):
    # Función GET que devuelve una instancia
    def get(self, request, id):
        entidad = get_object_or_404(EstatusEntidad.objects.all(), id=id)
        serializer = EntidadSerializer(entidad)
        return Response(serializer.data)

    # Función PUT que actualiza una instancia
    def put(self, request, id):
        entidad = get_object_or_404(EstatusEntidad.objects.all(), id=id)
        serializer = EntidadSerializer(entidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Función PATCH que actualiza parcialmente una instancia
    def patch(self, request, id):
        entidad = get_object_or_404(EstatusEntidad.objects.all(), id=id)
        serializer = EntidadSerializer(entidad, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Función DELETE para eliminar una instancia
    def delete(self, request, id):
        entidad = get_object_or_404(EstatusEntidad.objects.all(), id=id)
        entidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Vista del modelo Proyecto, que puede ser activo o inactivo
class ProyectoView(APIView):
    # Función GET que devuelve todos los objetos
    def get(self, request):
        proyectos = Proyecto.objects.all()
        serializer = ProyectoSerializer(proyectos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Función POST para crear un objeto
    def post(self, request):
        proyecto = ProyectoSerializer(data=request.data)
        if proyecto.is_valid():
            proyecto.save()
            return Response(proyecto.data, status=status.HTTP_201_CREATED)
        return Response(proyecto.errors, status=status.HTTP_400_BAD_REQUEST)


# Vista que devuelve unicamente trabaja con los datos de una instancia
class ProyectoDetalle(APIView):
    # Función GET que devuelve una instancia
    def get(self, request, id):
        proyecto = get_object_or_404(Proyecto.objects.all(), id=id)
        serializer = ProyectoSerializer(proyecto)
        return Response(serializer.data)

    # Función PUT que actualiza una instancia
    def put(self, request, id):
        proyecto = get_object_or_404(ProyectoSerializer.objects.all(), id=id)
        serializer = EntidadSerializer(proyecto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Función PATCH que actualiza parcialmente una instancia
    def patch(self, request, id):
        proyecto = get_object_or_404(Proyecto.objects.all(), id=id)
        serializer = ProyectoSerializer(proyecto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Función DELETE para eliminar una instancia
    def delete(self, request, id):
        entidad = get_object_or_404(EstatusEntidad.objects.all(), id=id)
        entidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Vista del modelo Proyecto, que puede ser activo o inactivo
class AreaView(APIView):
    # Función GET que devuelve todos los objetos
    def get(self, request):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Función POST para crear un objeto
    def post(self, request):
        area = AreaSerializer(data=request.data)
        if area.is_valid():
            area.save()
            return Response(area.data, status=status.HTTP_201_CREATED)
        return Response(area.errors, status=status.HTTP_400_BAD_REQUEST)


# Vista que devuelve unicamente trabaja con los datos de una instancia
class AreaDetalle(APIView):
    # Función GET que devuelve una instancia
    def get(self, request, id):
        area = get_object_or_404(Area.objects.all(), id=id)
        serializer = ProyectoSerializer(area)
        return Response(serializer.data)

    # Función PUT que actualiza una instancia
    def put(self, request, id):
        area = get_object_or_404(AreaSerializer.objects.all(), id=id)
        serializer = EntidadSerializer(area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Función PATCH que actualiza parcialmente una instancia
    def patch(self, request, id):
        area = get_object_or_404(Area.objects.all(), id=id)
        serializer = AreaSerializer(area, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Función DELETE para eliminar una instancia
    def delete(self, request, id):
        area = get_object_or_404(Area.objects.all(), id=id)
        area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Vista del modelo Proyecto, que puede ser activo o inactivo
class UsuarioView(APIView):
    # Función GET que devuelve todos los objetos
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Función POST para crear un objeto
    def post(self, request):
        usuario = UsuarioSerializer(data=request.data)
        if usuario.is_valid():
            usuario.save()
            return Response(usuario.data, status=status.HTTP_201_CREATED)
        return Response(usuario.errors, status=status.HTTP_400_BAD_REQUEST)


# Vista que devuelve unicamente trabaja con los datos de una instancia
class UsuarioDetalle(APIView):
    # Función GET que devuelve una instancia
    def get(self, request, id):
        usuario = get_object_or_404(Usuario.objects.all(), id=id)
        serializer = ProyectoSerializer(usuario)
        return Response(serializer.data)

    # Función PUT que actualiza una instancia
    def put(self, request, id):
        usuario = get_object_or_404(UsuarioSerializer.objects.all(), id=id)
        serializer = EntidadSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Función PATCH que actualiza parcialmente una instancia
    def patch(self, request, id):
        usuario = get_object_or_404(Usuario.objects.all(), id=id)
        serializer = AreaSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Función DELETE para eliminar una instancia
    def delete(self, request, id):
        usuario = get_object_or_404(Area.objects.all(), id=id)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)