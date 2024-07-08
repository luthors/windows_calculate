from rest_framework.viewsets import ModelViewSet
from main_app.api.view.alum_panel_section_view import AlumPanelSectionViewSet
from main_app.model.alum_artifact import AlumArtifact
from main_app.api.serializers import AlumArtifactPanelSerializer, AlumArtifactSerializer
from rest_framework import status
from rest_framework.response import Response
from main_app.model.alum_artifact_panel import AlumArtifactPanel



class AlumArtifactViewSet(ModelViewSet):
    model = AlumArtifact
    queryset = AlumArtifact.objects.all()
    serializer_class = AlumArtifactSerializer
    
    def create(self, request, *args, **kwargs):
        
    
"""     
    def create(self, request, *args, **kwargs):
        print ('=========================================================================')
        design= request.data['design']
        print('design: ', design)
        panels: dict = {}
        for char in design:
            if char in panels:
                panels[char] += 1
            else:
                panels[char] = 1
            print(panels)
            print(char)
        
        alum_artifact= AlumArtifactSerializer(data=request.data)
        alum_artifact.is_valid(raise_exception=True)
        alum_artifact.save()
        print('alum_artifact----: ',  alum_artifact.data)
        panel= {}
        for key, value in panels.items():
            panel['artifact_id'] = alum_artifact.data['id']
            panel['length'] = 0
            panel['amount_panel'] = value
            if key == 'X':
                panel['panel_type'] = 'MOVIL'
            elif key == 'O':
                panel['panel_type'] = 'FIJO'
            elif key == 'B':
                panel['panel_type'] = 'BATIENTE'
            elif key == 'P':
                panel['panel_type'] = 'PROYECTANTE'
            elif key == 'D':
                panel['panel_type'] = 'DESLIZANTE'
            elif key == 'M':
                panel['panel_type'] = 'MARCO'
            panel['width'] = request.data['width']
            panel['height'] = request.data['height']
            panel_serializer = AlumArtifactPanelSerializer(data=panel)
            panel_serializer.is_valid(raise_exception=True)
            panel_saved = panel_serializer.save()
        query_alum_artifact_panel = AlumArtifactPanel.objects.filter(artifact_id=alum_artifact.data['id'])
        for panel in query_alum_artifact_panel:
            print('panel: ', panel)
        print('query_alum_artifact_panel: ', query_alum_artifact_panel.values())
        return Response(data=alum_artifact.data, status= status.HTTP_201_CREATED)
 """
        # artifact_id = 
        
