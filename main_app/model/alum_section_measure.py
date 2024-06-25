
from django.db import models
from main_app.model.alum_section import AlumSection

class AlumSectionMeasure(models.Model):
    section_id = models.ForeignKey(AlumSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    milimeter = models.FloatField(default=0)
    inch = models.FloatField(default=0)
    
    