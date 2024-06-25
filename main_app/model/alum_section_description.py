
from django.db import models
from main_app.model.alum_system import AlumSystem

class AlumSectionDescription(models.Model):
    conect_id = models.ForeignKey(AlumSystem, on_delete=models.CASCADE)
    description_item = models.TextField()