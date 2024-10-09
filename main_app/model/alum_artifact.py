from django.db import models
from main_app.model.alum_system import AlumSystem
from main_app.model.enum.enums import ARTIFACT_TYPE


class AlumArtifact(models.Model):
    system_id = models.ForeignKey(AlumSystem, on_delete=models.CASCADE, related_name='system')
    name = models.CharField(max_length=50, blank=False)
    width = models.FloatField(default=0, blank=False)
    height = models.FloatField(default=0, blank=False)
    artifact_type = models.CharField(max_length=20, choices=ARTIFACT_TYPE, )
    design = models.CharField(max_length=10, blank=False)
    has_alfajia = models.BooleanField(default=False, )
    has_parche = models.BooleanField(default=False, )
    has_adapter = models.BooleanField(default=False, )
    