
from django.db import models
from main_app.model.alum_system import AlumSystem

class AlumSystemDescription(models.Model):
    system_id = models.ForeignKey(AlumSystem, on_delete=models.CASCADE, related_name='descriptions')
    description_item = models.TextField()