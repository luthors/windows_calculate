
from rest_framework import serializers
from main_app.api.services.AlumSystemService import AlumSystemService
from main_app.model.alum_system import AlumSystem
from main_app.model.alum_line import AlumLine
from main_app.model.alum_section import AlumSection
from main_app.model.alum_artifact import AlumArtifact
from main_app.model.alum_artifact_panel import AlumArtifactPanel
from main_app.model.alum_system_description import AlumSystemDescription
from main_app.model.alum_panel_section import AlumPanelSection

class AlumSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumSection
        fields = '__all__'

class AlumSystemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumSystemDescription
        fields = '__all__'

class AlumSystemSerializer(serializers.ModelSerializer):
    alum_system_service: AlumSystemService = None
    sections = AlumSectionSerializer(many=True, read_only=True)
    descriptions = AlumSystemDescriptionSerializer(many=True, read_only=True)
    
    class Meta:
        model = AlumSystem
        fields = '__all__'
""" 
    def create(self, validated_data):
        return self.alum_system_service.create_alum_system(validated_data)

    def get_all(self):
        return self.alum_system_service.get_all()
    
    def get_by_id(self, id):
        return self.alum_system_service.get_by_id(id)
    
    def get_by_name(self, name):
        #retornar varios registros
        
        return self.alum_system_service.get_by_name(name)

 """
class AlumLineSerializer(serializers.ModelSerializer):
    systems = AlumSystemSerializer(many=True, read_only=True)
    class Meta:
        model = AlumLine
        fields = '__all__'

class AlumArtifactPanelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AlumArtifactPanel
        fields = '__all__'

class AlumArtifactSerializer(serializers.ModelSerializer):
    panels = AlumArtifactPanelSerializer(many=True, read_only=True)
    class Meta:
        model = AlumArtifact
        fields = '__all__'

class AlumPanelSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumPanelSection
        fields = '__all__'





