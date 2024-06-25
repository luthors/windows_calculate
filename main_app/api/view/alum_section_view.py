from rest_framework.viewsets import ModelViewSet
from main_app.model.alum_section import AlumSection
from main_app.api.serializers import AlumSectionSerializer

class AlumSectionViewSet(ModelViewSet):
    model = AlumSection
    queryset = AlumSection.objects.all()
    serializer_class = AlumSectionSerializer
    fields = '__all__'
