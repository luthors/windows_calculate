from .interfaces import IAlumArtifactService
from main_app.model.alum_artifact import AlumArtifact
from typing import Dict, Any

class AlumArtifactService(IAlumArtifactService):
    def create_alum_artifact(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return AlumArtifact.objects.create(**data)
    