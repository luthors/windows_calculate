from django.db import models
from main_app.model.alum_section import AlumSection
from main_app.model.alum_artifact_panel import AlumArtifactPanel

class AlumPanelSection(models.Model):
    artifact_panel_id = models.ForeignKey(AlumArtifactPanel, on_delete=models.CASCADE)
    section_id = models.ForeignKey(AlumSection, on_delete=models.CASCADE)
    length = models.FloatField(default=0)
    amount = models.IntegerField(default=0)

    