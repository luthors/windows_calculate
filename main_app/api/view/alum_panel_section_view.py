from rest_framework.viewsets import ModelViewSet
from main_app.model.alum_panel_section import AlumPanelSection
from main_app.api.serializers import AlumPanelSectionSerializer
from rest_framework import status
from rest_framework.response import Response

class AlumPanelSectionViewSet(ModelViewSet):
    model = AlumPanelSection
    queryset = AlumPanelSection.objects.all()
    serializer_class = AlumPanelSectionSerializer
    
    
    def create(self, request, *args, **kwargs):
        print('entre a la funcion')
        print('request====> ', request)
        alum_panel_section = {}
        alum_panel_section['length'] = request['length']
        alum_panel_section['artifact_panel_id'] = request['id']
        
        
                           
        
        
        return Response(status=status.HTTP_201_CREATED)
