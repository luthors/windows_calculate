from rest_framework.viewsets import ModelViewSet
from main_app.model.alum_artifact_panel import AlumArtifactPanel
from main_app.api.serializers import AlumArtifactPanelSerializer

class AlumArtifactPanelViewSet(ModelViewSet):
    model = AlumArtifactPanel
    queryset = AlumArtifactPanel.objects.all()
    serializer_class = AlumArtifactPanelSerializer
    fields = '__all__'

    def create(self, request, *args, **kwargs):
        serializer_panel = AlumArtifactPanelSerializer(data=request.data)
        serializer_panel.is_valid(raise_exception=True)
        serializer_panel.save()
        
        
        
        