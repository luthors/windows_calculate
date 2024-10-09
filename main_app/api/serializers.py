
from rest_framework import serializers, status
from main_app.api.config.config_var import LETTERS_TYPES_LIST, LETTERS_TYPES_SLIDING
from main_app.api.services.AlumSystemService import AlumSystemService

from main_app.model.alum_system import AlumSystem
from main_app.model.alum_line import AlumLine
from main_app.model.alum_section import AlumSection
from main_app.model.alum_artifact import AlumArtifact
from main_app.model.alum_artifact_panel import AlumArtifactPanel
from main_app.model.alum_system_description import AlumSystemDescription
from main_app.model.alum_panel_section import AlumPanelSection
from main_app.model.enum.enums import ARTIFACT_TYPE

class AlumSectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AlumSection
        fields = '__all__'

class AlumSystemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumSystemDescription
        fields = '__all__'

class AlumSystemSerializer(serializers.ModelSerializer):
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

class AlumPanelSectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AlumPanelSection
        fields = '__all__'

class AlumArtifactPanelSerializer(serializers.ModelSerializer):
    sections = AlumPanelSectionSerializer(many=True, read_only=True)
    class Meta:
        model = AlumArtifactPanel
        fields = '__all__'

class AlumArtifactSerializer(serializers.ModelSerializer):
    panels = AlumArtifactPanelSerializer(many=True, read_only=True)
    class Meta:
        model = AlumArtifact
        fields = '__all__'
    def validate_design(self, value):
        is_sliding = self.initial_data.get('artifact_type') == ARTIFACT_TYPE[0][0]
        len_design = len(value)
        letters_valides = LETTERS_TYPES_LIST
        letters_valides_sliding = LETTERS_TYPES_SLIDING
        if is_sliding:
            if len_design <= 1:
                raise serializers.DjangoValidationError(message="Invalid design: El diseño corrediza debe tener al menos 2 paneles", code='HTTP_406_NOT_ACCEPTABLE')
            
            for letter in value:
                if  not letter.upper() in letters_valides_sliding:
                    raise serializers.ValidationError("Invalid design: El diseño corrediza solo puede tener paneles de tipo: {}".format(LETTERS_TYPES_SLIDING))
            
        for letter in value:
            if  not letter.upper() in letters_valides:
                raise serializers.ValidationError("Invalid design: las letras solo pueden ser: {}".format(LETTERS_TYPES_LIST))
        return value.upper()
    

