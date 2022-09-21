from django.db import models

# Create your models here.
class libro(models.Model):
    title = models.CharField(max_length=100)
    resume = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    copia = models.IntegerField()