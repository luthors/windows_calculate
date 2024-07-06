
from django.db import models
from main_app.model.alum_section import AlumSection

class AlumSectionDescription(models.Model):
    conect_id = models.ForeignKey(AlumSection, on_delete=models.CASCADE, related_name='descriptions')
    description_item = models.TextField()