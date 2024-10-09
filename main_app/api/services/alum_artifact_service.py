""" from main_app.api.config.config_var import ALUM_SYSTEMS_LIST_SLIDING, LETTERS_TYPES_SLIDING
from main_app.api.serializers import AlumArtifactPanelSerializer
from main_app.model.alum_artifact_panel import AlumArtifactPanel
from main_app.model.alum_system import AlumSystem
from main_app.model.enum.enums import PANEL_TYPE
from .interfaces import IAlumArtifactService
from main_app.model.alum_artifact import AlumArtifact
from typing import Dict, Any
from rest_framework import status

class AlumArtifactService(IAlumArtifactService):
    def create_alum_artifact(self, data: Dict[str, Any], id_alum_artifact: int) -> Dict[str, Any]:
        id_alum_system=data['system_id']
        alum_system_code = AlumSystem.objects.get(id=id_alum_system).code
        panels_count = len(data['design'])
        print('X'*100)
        print('panels_count: ', panels_count)
        print('alum_system_code: ', alum_system_code)
        response = {}
        panel_new={}
        width = 0
        height = 0
        #aqui necesito guardar el alumartifact en la base de datos
        #print('alum_artifact: ', alum_artifact)
        if alum_system_code in ALUM_SYSTEMS_LIST_SLIDING:
            panels_x_count = data['design'].upper().count('X') or 0
            panels_o_count = data['design'].upper().count('O') or 0
            panels_p_count = data['design'].upper().count('P') or 0
            if alum_system_code == ALUM_SYSTEMS_LIST_SLIDING[1]:
                print("es 5020")
                panel_new['width'] =  float(data['width'])/2
                panel_new['height'] = float(data['height'])-1.3
                if panels_x_count > 0:
                    panel_new['amount_panel'] = panels_x_count
                    panel_new['panel_type'] = 2
                    panel_new['artifact_id'] = id_alum_artifact
                    
                    alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                    print('alum_artifact_panel_serializer: ', alum_artifact_panel_serializer)
                    alum_artifact_panel_serializer.is_valid(raise_exception=True)
                    alum_artifact_panel_serializer.save()
                    print('panel_new: ', panel_new)
                if panels_o_count > 0:
                    panel_new['amount_panel'] = panels_o_count
                    panel_new['panel_type'] = PANEL_TYPE[1]
                    print('panel_new: ', panel_new)
                if panels_p_count > 0:
                    panel_new['amount_panel'] = panels_p_count
                    panel_new['panel_type'] = PANEL_TYPE[2]
                    print('panel_new: ', panel_new)
                
            elif alum_system_code == ALUM_SYSTEMS_LIST_SLIDING[2]:
                print("es 744")
            elif alum_system_code == ALUM_SYSTEMS_LIST_SLIDING[3]:
                print("es 8025")
            elif alum_system_code == ALUM_SYSTEMS_LIST_SLIDING[4]:
                print("es 7038")
            elif alum_system_code == ALUM_SYSTEMS_LIST_SLIDING[0]:
                print("es 3825")
                
            
            if panels_x_count > panels_count or panels_o_count > panels_count or panels_p_count > panels_count:
                print("400 Bad Request")
                
            
            
                
            
            
            
            
            
        else:
            print("400 Bad Request")
            return ("400 Bad Request")
            
        return data
        #return AlumArtifact.objects.create(**data)
     """