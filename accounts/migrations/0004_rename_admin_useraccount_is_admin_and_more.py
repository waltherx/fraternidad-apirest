# Generated by Django 4.2.3 on 2023-09-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_active_useraccount_is_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='admin',
            new_name='is_admin',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
