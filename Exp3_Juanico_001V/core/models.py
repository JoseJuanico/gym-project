from django.db import models


# Create your models here.
class Tipo(models.Model):
    idTipoUsuario = models.IntegerField(primary_key = True, verbose_name='Id del usuario') #se da relacion con usuario
    tipo = models.CharField(max_length = 20, verbose_name = 'Tipo de usuario')

    def __str__(self):
        return self.tipo

class Usuario(models.Model):
    rut = models.CharField (max_length = 10,primary_key = True, verbose_name = 'Rut del usuario') #verbosename es lo que sale como un label en lapaginas
    nombre = models.CharField (max_length = 50, verbose_name = 'Nombre usuario')
    apellido = models.CharField (max_length = 50, verbose_name = 'Apellido usuario')
    correo = models.EmailField (max_length = 50,verbose_name = 'Correo electrónico')
    contrasena = models.CharField (max_length = 9, verbose_name = 'contraseña')
    tipo = models.ForeignKey (Tipo, on_delete=models.CASCADE) 
   
    def __str__(self): # metodo toString
        return self.rut

