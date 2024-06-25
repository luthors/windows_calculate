
from django.db import models

class AlumLine(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Linea'
        verbose_name_plural = 'Lineas'
    
    def __str__(self):
        return str(self.id) + " - " + self.name

    