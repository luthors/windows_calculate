import rest_framework
from rest_framework import viewsets, generics

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

class AlumSystemDescriptionViewSet(viewsets.ModelViewSet):
    queryset = AlumSystemDescription.objects.all()
    serializer_class = AlumSystemDescriptionSerializer
    
        

