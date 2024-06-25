
from django.db import models
from main_app.model.alum_system import AlumSystem

class AlumSection(models.Model):
    system_id= models.ForeignKey(AlumSystem, on_delete=models.CASCADE, related_name='sections')
    sku = models.CharField(max_length=20, unique=True)
    optional_code= models.CharField(max_length=20, unique=True)
    length = models.FloatField(default=0)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    common_name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        
    def __str__(self):
        return str(self.id) + " - " + self.sku + " - " + self.title 