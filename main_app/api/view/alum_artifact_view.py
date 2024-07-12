from rest_framework.viewsets import ModelViewSet
from main_app.api.services.alum_artifact_service import AlumArtifactService
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
    
    """ def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        
        alum_artifact_service = AlumArtifactService()        
        serializer = serializer_class(*args, **kwargs)
        serializer.alum_artifact_service = alum_artifact_service
        return serializer
     """
    def create(self, request, *args, **kwargs):
        print('request: ', request)
        print('*'*100)
        print('request.__dict__: ', request.__dict__)
        print('*'*100)
        alum_artifact_service = AlumArtifactService()
        serializer = self.serializer_class(data=request.data)
        print('serializer: ', serializer)
        serializer.alum_artifact_service = alum_artifact_service
        r=serializer.alum_artifact_service.create_alum_artifact(request.data)
        print('r: ', r)
        print('type(r): ', type(r))
        print('alum_artifact_service: ', alum_artifact_service.__dict__)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
              
    
        
