# Generated by Django 5.2.1 on 2025-05-31 16:53

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
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('categoria', models.CharField(choices=[('pan', 'Pan'), ('dulce', 'Dulce')], max_length=50)),
                ('ingredientes', models.TextField()),
                ('preparacion', models.TextField()),
                ('tiempo_preparacion', models.PositiveIntegerField(help_text='Tiempo en minutos')),
                ('dificultad', models.CharField(choices=[('facil', 'Fácil'), ('medio', 'Medio'), ('dificil', 'Difícil')], max_length=50)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='recetas/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
