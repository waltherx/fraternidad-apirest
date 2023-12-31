# Generated by Django 4.2.3 on 2023-09-08 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fraternidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('color', models.CharField(default='', max_length=7, null=True)),
                ('direccion', models.CharField(default='', max_length=300, null=True)),
                ('mensualidad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('monto_suspendido', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('monto_no_reserva', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('turno_semanal', models.CharField(default='', max_length=50)),
                ('banco', models.CharField(default='', max_length=150, null=True)),
                ('nro_cuenta', models.CharField(default='', max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=10)),
                ('url', models.URLField(max_length=700)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('fraternidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.fraternidad')),
            ],
        ),
        migrations.CreateModel(
            name='Cumpleanio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponible', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
