# Generated by Django 4.2.7 on 2024-02-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0003_remove_mensualidad_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallepagoevento',
            name='canselado',
            field=models.BooleanField(default=False),
        ),
    ]
