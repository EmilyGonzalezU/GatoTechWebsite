from django.db import models

class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=90, unique=True)
    rut = models.CharField(max_length=12, unique=True)
    contrasena = models.CharField(max_length=128)

    def __str__(self):
        return self.email
    
    
