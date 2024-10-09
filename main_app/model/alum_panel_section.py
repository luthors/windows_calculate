from django.db import models
from main_app.model.alum_section import AlumSection
from main_app.model.alum_artifact_panel import AlumArtifactPanel

class AlumPanelSection(models.Model):
    artifact_panel_id = models.ForeignKey(AlumArtifactPanel, on_delete=models.CASCADE, related_name='sections')
    section_id = models.ForeignKey(AlumSection, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50, default="")
    length = models.FloatField(default=0)
    amount = models.IntegerField(default=0)

    