from django.db import models
from django.conf import settings

# Create your models here.
Usuario_Blog = settings.AUTH_USER_MODEL

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=4)

    @classmethod
    def get_default_values(cls):
        return Pais.objects.get(id=1)

    def __str__(self):
        return self.nombre

class Tag(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Posts(models.Model):
    user = models.ForeignKey(Usuario_Blog, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag)
    contenido = models.TextField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    actualizo_el = models.DateField(null=True)

    class Meta:
        ordering = ['-fecha_de_creacion']

    def __str__(self):
        return self.titulo