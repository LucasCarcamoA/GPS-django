# Generated by Django 5.1.3 on 2024-11-23 21:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('telefono', models.BigIntegerField()),
                ('tipo_usuario', models.CharField(choices=[('', 'Seleccione un tipo de usuario'), ('Administrador', 'Administrador'), ('Conductor', 'Conductor')], max_length=50)),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], max_length=10)),
                ('device', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GPSLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gps_logs', to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=6, unique=True)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anno', models.IntegerField()),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to='app.usuario')),
            ],
        ),
    ]