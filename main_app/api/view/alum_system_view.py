from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from main_app.api.services.AlumSystemService import AlumSystemService
from main_app.model.alum_system import AlumSystem
from main_app.model.alum_line import AlumLine
from main_app.model.alum_section import AlumSection
from main_app.model.alum_artifact import AlumArtifact
from main_app.model.alum_artifact_panel import AlumArtifactPanel

from main_app.api.serializers import (AlumArtifactPanelSerializer, AlumArtifactSerializer,
    AlumLineSerializer, AlumSectionSerializer, AlumSystemDescriptionSerializer,
    AlumSystemSerializer)
from main_app.model.alum_system_description import AlumSystemDescription

class AlumSystemViewSet(viewsets.ModelViewSet):
    queryset = AlumSystem.objects.all()
    serializer_class = AlumSystemSerializer
    """ 
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        
        alum_system_service = AlumSystemService()
        serializer = serializer_class(*args, **kwargs)
        serializer.alum_system_service = alum_system_service
        return serializer
    
    @action(detail=False, methods=['get'], url_path='get_by_name/(?P<name>[^/.]+)')
    def get_alum_systems_by_name(self, request, name=None):
        alum_system_service = AlumSystemService()
        alum_system = alum_system_service.get_by_name(name)
        if alum_system:
            serializer = self.get_serializer(alum_system)
            return Response(serializer.data)
        return self.serializer_class.get_by_name(name)
    """

class AlumSystemDescriptionViewSet(viewsets.ModelViewSet):
    queryset = AlumSystemDescription.objects.all()
    serializer_class = AlumSystemDescriptionSerializer
    
        

