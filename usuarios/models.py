from django.db import models

class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=90, unique=True)
    rut = models.CharField(max_length=12, unique=True)
<<<<<<< HEAD
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email
=======
    contrasena = models.CharField(max_length=128)

    def __str__(self):
        return self.email
    
    
class Direccion(models.Model):
    perfil_usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    depto_casa = models.CharField(max_length=10, blank=True, null=True)
    nombre_receptor = models.CharField(max_length=60)
    apellido_receptor = models.CharField(max_length=60)
    rut_receptor = models.CharField(max_length=12)
    telefono_receptor = models.CharField(max_length=15)
    region = models.CharField(max_length=15, null=False)
    comuna = models.CharField(max_length=15, null=False)

    def __str__(self):
        return f'{self.calle} {self.numero}, {self.comuna}, {self.region}'
>>>>>>> cambios
