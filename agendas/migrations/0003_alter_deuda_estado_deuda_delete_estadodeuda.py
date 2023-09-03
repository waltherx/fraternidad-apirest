# Generated by Django 4.2.3 on 2023-09-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0002_delete_detalledeuda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deuda',
            name='estado_deuda',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('pagada', 'Pagada')], default='pendiente', max_length=15),
        ),
        migrations.DeleteModel(
            name='EstadoDeuda',
        ),
    ]
