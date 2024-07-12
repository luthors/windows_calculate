
from rest_framework import serializers
from main_app.api.config.config_var import LETTERS_TYPES_LIST
from main_app.api.services.AlumSystemService import AlumSystemService
from main_app.api.services.alum_artifact_service import AlumArtifactService
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
    alum_artifact_service: AlumArtifactService = None
    class Meta:
        model = AlumArtifact
        fields = '__all__'
    def validate_design(self, value):
        print("============================================")
        print('self.initial_data.get(artifact_type):' , self.initial_data.get('artifact_type'))
        print('ARTIFACT_TYPE.CORREDIZA: ', ARTIFACT_TYPE[0][0])
        
        is_sliding = self.initial_data.get('artifact_type') == ARTIFACT_TYPE[0][0]
        print('self.context: ', self.context)
        len_design = len(value)
        print('is_sliding: ', is_sliding)
        letters_valides = LETTERS_TYPES_LIST
        
        if len_design <= 1 and is_sliding:
            raise serializers.ValidationError("Invalid design: debe tener mas de una letra")
        for letter in value:
            if  not letter.upper() in letters_valides:
                raise serializers.ValidationError("Invalid design: las letras solo pueden ser: {}".format(LETTERS_TYPES_LIST))
        return value.upper()
    def create(self, validated_data):
        print('@'*100)
        response = self.alum_artifact_service.create_alum_artifact(validated_data)
        print('response: ', response)
        print('type(response): ', type(response))
        if type(response) == Exception:
            print('response: ', response)
            raise serializers.ValidationError(response)
        return 
    

class AlumPanelSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumPanelSection
        fields = '__all__'





