from django.conf import settings
from django.db import models
from django.utils.html import mark_safe

class Notificacion(models.Model):
    titulo = models.CharField(max_length=300, default="", null=False)
    descripcion = models.TextField(default="", null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    user_destino = models.IntegerField(default=-1)
    user_remitente = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    leido = models.BooleanField(default=False)


class Token(models.Model):
    token = models.TextField(default="", null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Cumpleanio(models.Model):
    disponible = models.BooleanField(default=False)
    fecha = models.DateTimeField(null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Cumpleanio : {self.user.username}"


class Fraternidad(models.Model):
    nombre = models.CharField(max_length=100, default="", null=False)
    color = models.CharField(max_length=7, default="", null=True)
    direccion = models.CharField(max_length=300, default="", null=True)
    mensualidad = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False
    )
    monto_suspendido = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False
    )
    monto_no_reserva = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False
    )
    turno_semanal = models.CharField(max_length=50, default="", null=False)
    banco = models.CharField(max_length=150, default="", null=True)
    nro_cuenta = models.CharField(max_length=150, default="", null=True)

    def __str__(self) -> str:
        return f"Fraternidad : {self.nombre}"


class Medio(models.Model):
    MEDIA_TYPES = (
        ("image", "Image"),
        ("video", "Video"),
    )

    tipo = models.CharField(max_length=10, choices=MEDIA_TYPES)
    url = models.URLField(max_length=500)
    descripcion = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    fraternidad = models.ForeignKey(Fraternidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"Medio : {self.descripcion},  Tipo:  {self.tipo} "

    def image_tag(self):
        if self.tipo == "Image":
            return mark_safe(
                f"<div style='width: 200px; height: 200px; display: flex; justify-content: center; align-items: center; overflow: hidden;'><img src='{self.url}' alt='Mi imagen' style='width: 100%; height: auto;'></div>"
            )
        else:
            return mark_safe(
                f"<iframe width='200' height='200' src='{self.url}' ></iframe>"
            )
