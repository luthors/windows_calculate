from django.db import models
from main_app.model.alum_line import AlumLine

class AlumSystem(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    line_id = models.ForeignKey(AlumLine, on_delete=models.CASCADE, related_name='systems')
    
    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'
    def __str__(self):
        return str(self.id) + " - " + self.name
    