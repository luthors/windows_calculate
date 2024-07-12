from main_app.api.config.config_var import ALUM_SYSTEMS_LIST_SLIDING
from main_app.model.alum_system import AlumSystem
from .interfaces import IAlumArtifactService
from main_app.model.alum_artifact import AlumArtifact
from typing import Dict, Any
from rest_framework import status

class AlumArtifactService(IAlumArtifactService):
    def create_alum_artifact(self, data: Dict[str, Any]) -> Dict[str, Any]:
        id=data['system_id']
        alum_system_code = AlumSystem.objects.get(id=id).code
        print('-'*100)
        print('alum_system_code: ', alum_system_code)
        response = {}
        if alum_system_code in ALUM_SYSTEMS_LIST_SLIDING:
            print('entre al if es un sliding')
            if len(data['design'])<=1:
                response['status'] = status.HTTP_406_NOT_ACCEPTABLE
                response['message'] = 'The design must have at least 2 panels'
                return Exception(response)
            
        else:
            print("400 Bad Request")
            return ("400 Bad Request")
            
        return data
        #return AlumArtifact.objects.create(**data)
    