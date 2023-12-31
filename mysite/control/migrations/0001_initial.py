# Generated by Django 4.2 on 2023-08-03 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('departamento', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('dias_trabajo', models.CharField(max_length=100)),
                ('turno', models.CharField(choices=[('Dia', 'Día'), ('Tarde', 'Tarde'), ('Noche', 'Noche')], max_length=10)),
                ('horario_entrada', models.TimeField()),
                ('horario_salida', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('identificador', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('tipo_marcacion', models.CharField(choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], max_length=10)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.empleado')),
            ],
        ),
    ]
