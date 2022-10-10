from django.db import models

# Create your models here.
class Imprenta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

################# Relacion de uno a muchos donde la llave muchos pasa para el lado uno ######

class Libro(models.Model):
    title = models.CharField(max_length=100)
    resume = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    copia = models.IntegerField()
    id_imprenta = models.ForeignKey(Imprenta, related_name='libros', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'

    def __str__(self):
        return self.title

####################################### ManyToMany ##############################

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    libros = models.ManyToManyField(Libro)

    def __str__(self):
        return self.nombre



######################## Relacion OneToOne ####################################
class Lector(models.Model):
    nombre=models.CharField(max_length=100)
    libro_ocupado = models.OneToOneField(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

