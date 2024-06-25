from rest_framework.viewsets import ModelViewSet
from main_app.model.alum_line import AlumLine
from main_app.api.serializers import AlumLineSerializer

class AlumLineViewSet(ModelViewSet):
    model = AlumLine
    queryset = AlumLine.objects.all()
    serializer_class = AlumLineSerializer
    fields = '__all__'