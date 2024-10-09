from django.db import models
from main_app.model.alum_artifact import AlumArtifact
from main_app.model.alum_section import AlumSection
from main_app.model.enum.enums import PANEL_TYPE

class AlumArtifactPanel(models.Model):
    
    artifact_id = models.ForeignKey(AlumArtifact, on_delete=models.CASCADE, related_name='panels')
    length = models.FloatField(default=0)
    amount_panel = models.IntegerField(default=0)
    panel_type = models.CharField(max_length=20, choices= PANEL_TYPE,)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    position = models.IntegerField(default=0)