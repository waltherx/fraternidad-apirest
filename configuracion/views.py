from rest_framework import viewsets
from .models import (
    Cumpleanio,
    Fraternidad,
    MediaImage,
    MediaVideo,
    Articulo,
    Horario,
    Actividad,
    DiaSemana,
    Cronograma,
)
from .serializers import (
    CumpleanioSerializer,
    FraternidadSerializer,
    MediaImageSerializer,
    MediaVideoSerializer,
    ArticuloSerializer,
    # NotificacionSerializer,
    # TokenSerializer,
    ActividadSerializer,
    HorarioSerializer,
    CronogramaSerializer,
    DiaSemanaSerializer,
)


class CumpleanioView(viewsets.ModelViewSet):
    serializer_class = CumpleanioSerializer
    queryset = Cumpleanio.objects.all()


"""
class TokenView(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()

class NotificacionView(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    queryset = Notificacion.objects.all()
"""


class FraternidadView(viewsets.ModelViewSet):
    serializer_class = FraternidadSerializer
    queryset = Fraternidad.objects.all()


class MediaImageView(viewsets.ModelViewSet):
    serializer_class = MediaImageSerializer
    queryset = MediaImage.objects.all()


class MediaVideoView(viewsets.ModelViewSet):
    serializer_class = MediaVideoSerializer
    queryset = MediaVideo.objects.all()


class ArticuloView(viewsets.ModelViewSet):
    serializer_class = ArticuloSerializer
    queryset = Articulo.objects.all()


class ArticuloView(viewsets.ModelViewSet):
    serializer_class = ArticuloSerializer
    queryset = Articulo.objects.all()


class ArticuloView(viewsets.ModelViewSet):
    serializer_class = ArticuloSerializer
    queryset = Articulo.objects.all()


class ArticuloView(viewsets.ModelViewSet):
    serializer_class = ArticuloSerializer
    queryset = Articulo.objects.all()


class ActividadView(viewsets.ModelViewSet):
    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()


class DiaSemanaView(viewsets.ModelViewSet):
    serializer_class = DiaSemanaSerializer
    queryset = DiaSemana.objects.all()


class HorarioView(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer
    queryset = Horario.objects.all()


class CronogramaView(viewsets.ModelViewSet):
    serializer_class = CronogramaSerializer
    queryset = Cronograma.objects.all()
