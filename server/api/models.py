from django.db import models
from .choices import Estatus, Roles, Prioridades, TicketEstatus


class EstatusEntidad(models.Model):
    tipo = models.CharField(max_length=10, choices=Estatus, default="Inactivo")
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(null=True)


class EstatusTicket(models.Model):
    tipo = models.CharField(max_length=15, choices=TicketEstatus)
    creacion = models.DateTimeField(auto_now_add=True)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_final = models.DateTimeField(null=True)
    estatus = models.ForeignKey(EstatusEntidad, on_delete=models.DO_NOTHING)


class Area(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=10)
    descripcion = models.TextField(null=True, blank=True)
    proyecto = models.ManyToManyField(Proyecto)
    estatus = models.ForeignKey(EstatusEntidad, on_delete=models.DO_NOTHING)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(null=True)


class Rol(models.Model):
    tipo = models.CharField(max_length=2, choices=Roles, default="UO")
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(null=True)


class Prioridad(models.Model):
    tipo = models.CharField(max_length=10, choices=Prioridades, default="Baja")
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(null=True)


class Especialidad(models.Model):
    tipos = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(null=True)


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    materno = models.CharField(max_length=50)
    paterno = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.DO_NOTHING)
    estatus = models.ForeignKey(EstatusEntidad, on_delete=models.DO_NOTHING)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(null=True)


class Especialista(models.Model):
    especialidad = models.ManyToManyField(Especialidad)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(null=True)


class Ticket(models.Model):
    titulo = models.CharField(max_length=100)
    folio = models.CharField(max_length=10, unique=True)
    autor = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    especialista = models.ForeignKey(Especialista, on_delete=models.DO_NOTHING)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.DO_NOTHING)
    estatus = models.ForeignKey(EstatusTicket, on_delete=models.DO_NOTHING)
    coordenadas = models.TextField()
    # Fechas:
    creacion = models.DateTimeField(auto_now_add=True)
    atendido = models.DateTimeField(null=True)
    asignado = models.DateTimeField(null=True)
    proceso = models.DateTimeField(null=True)
    cancelado = models.DateTimeField(null=True)
    reasignado = models.DateTimeField(null=True)
    resuelto = models.DateTimeField(null=True)
    validado = models.DateTimeField(null=True)


class Evidencia(models.Model):
    evidencia = models.BinaryField()
    ticket = models.ManyToManyField(Ticket)


class Comentario(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now=True)
