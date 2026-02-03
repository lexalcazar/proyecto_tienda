from django.db import models

# Create your models here.
# marca instrumento
class Marca(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.pais_origen})"
    
# Modelo instrumento
class Instrumento(models.Model):
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    etiquetas = models.ManyToManyField('Etiqueta', blank=True)
    def __str__(self):
        return f"{self.nombre} - {self.tipo} - ${self.precio} - Marca: {self.marca.nombre} - Stock: {self.stock}"

# Modelo etiqueta
class Etiqueta(models.Model):
    
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre