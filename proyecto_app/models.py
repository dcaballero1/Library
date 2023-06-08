from django.db import models

# Create your models here.
class Printing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    owner = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

################# OneToMany #################################################

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    resume = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    copies = models.IntegerField()
    name_imprenta = models.ForeignKey(Printing, related_name='books', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title

####################################### ManyToMany #############################

class BookStore(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    owner= models.CharField(max_length=250)
    active = models.CharField(max_length=250)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


######################## OneToOne ###############################################

class Reader(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    state=models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    has_book = models.OneToOneField(Book, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

