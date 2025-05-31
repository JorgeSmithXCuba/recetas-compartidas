from django.db import models
from django.contrib.auth.models import User


class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50, choices=[('pan', 'Pan'), ('dulce', 'Dulce')])
    # categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    ingredientes = models.TextField()
    preparacion = models.TextField()
    tiempo_preparacion = models.PositiveIntegerField(help_text="Tiempo en minutos")
    dificultad = models.CharField(max_length=50, choices=[
        ('facil', 'Fácil'),
        ('medio', 'Medio'),
        ('dificil', 'Difícil')
    ])
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='recetas/', null=True, blank=True)

    def __str__(self):
        return self.titulo