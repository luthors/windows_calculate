from rest_framework.viewsets import ModelViewSet
from main_app.model.alum_panel_section import AlumPanelSection
from main_app.api.serializers import AlumPanelSectionSerializer
from rest_framework import status
from rest_framework.response import Response

class AlumPanelSectionViewSet(ModelViewSet):
    model = AlumPanelSection
    queryset = AlumPanelSection.objects.all()
    serializer_class = AlumPanelSectionSerializer
      
                           
    
        
    
