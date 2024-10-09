from rest_framework.viewsets import ModelViewSet
from main_app.api.config.config_var import ALUM_SYSTEMS_LIST_SLIDING, DESIGN_TYPES_5020
from main_app.api.view.alum_panel_section_view import AlumPanelSectionViewSet
from main_app.model.alum_artifact import AlumArtifact
from main_app.api.serializers import AlumArtifactPanelSerializer, AlumArtifactSerializer, AlumPanelSectionSerializer
from rest_framework import status
from rest_framework.response import Response
from main_app.model.alum_artifact_panel import AlumArtifactPanel
from main_app.model.alum_section import AlumSection
from main_app.model.alum_system import AlumSystem
from main_app.model.enum.enums import PANEL_TYPE

class AlumArtifactViewSet(ModelViewSet):
    model = AlumArtifact
    queryset = AlumArtifact.objects.all()
    serializer_class = AlumArtifactSerializer

    def create(self, request, *args, **kwargs):
        design = request.data['design']
        serializer = self.serializer_class(data=request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        id_alum_artifact = serializer.data['id']
        panels_count = len(design)
        response = {}
        panel_new={}
        id_alum_system = serializer.data['system_id']
        alum_system_code = AlumSystem.objects.get(id=id_alum_system).code
        data = serializer.data
        panel_new['artifact_id'] = id_alum_artifact
        if alum_system_code in ALUM_SYSTEMS_LIST_SLIDING:
            if not design in DESIGN_TYPES_5020:
                response['message'] = 'Design type not allowed'
                response['status'] = status.HTTP_406_NOT_ACCEPTABLE
                return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)
            panels_x_count = data['design'].upper().count('X') or 0
            panels_o_count = data['design'].upper().count('O') or 0
            panels_p_count = data['design'].upper().count('P') or 0
            if alum_system_code == ALUM_SYSTEMS_LIST_SLIDING[1]:  # 5020
                if panels_x_count > 0:
                    string_index = 0
                    for i in range(panels_x_count):    # CORREDIZAS - MOVILES
                        print('i: ', i)
                        print('design: ', design)
                        string_index = design.index('X',i if i == 0 else string_index+1)
                        print('string_index: ', string_index)
                        #panel_new['width'] =  (float(data['width']))/2
                        #panel_new['height'] = float(data['height'])-3.2
                        panel_new['position'] = string_index + 1
                        panel_new['amount_panel'] = panels_x_count
                        panel_new['panel_type'] = PANEL_TYPE[0][0]
                        print('panel_new: ', panel_new)
                        #print('alum_artifact_panel_serializer: ', alum_artifact_panel_serializer)
                        if design in ['XX','OX','XO']:
                            panel_new['width'] =  (float(data['width']))/2
                            panel_new['height'] = float(data['height'])-3.2
                            alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                            alum_artifact_panel_serializer.is_valid(raise_exception=True)
                            alum_artifact_panel_serializer.save()
                            artifact_panel_id = alum_artifact_panel_serializer.data['id']
                            # panel sections traslape
                            alum_panel_section={}
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0192').id # traslape
                            alum_panel_section['length'] = panel_new['height']
                            alum_panel_section['amount'] = 1
                            alum_panel_section['artifact_panel_id'] = artifact_panel_id
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections enganche
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0147').id # enganche
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections zocalo
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0349').id # zocalo
                            alum_panel_section['length'] = (float(data['width'])-2.5)/2
                            alum_panel_section['amount'] = 2
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                        if design in['PXX','XXP','XOX']:
                            panel_new['width'] =  (float(data['width']))/3
                            panel_new['height'] = float(data['height'])-3.2
                            alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                            alum_artifact_panel_serializer.is_valid(raise_exception=True)
                            alum_artifact_panel_serializer.save()
                            artifact_panel_id = alum_artifact_panel_serializer.data['id']
                            alum_panel_section={}
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0192').id if panel_new['position'] == 1\
                                else AlumSection.objects.get(sku='ALN0147').id # traslape o enganche según sea el caso
                            alum_panel_section['length'] = panel_new['height']
                            alum_panel_section['amount'] = 1
                            alum_panel_section['artifact_panel_id'] = artifact_panel_id
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections enganche
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0147').id # enganche
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections zocalo
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0349').id # zocalo
                            alum_panel_section['length'] = (float(data['width'])-2.5)/3
                            alum_panel_section['amount'] = 2
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                        if design in ['OXXO']:
                            panel_new['width'] =  (float(data['width']))/4
                            panel_new['height'] = float(data['height'])-3.2
                            alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                            alum_artifact_panel_serializer.is_valid(raise_exception=True)
                            alum_artifact_panel_serializer.save()
                            artifact_panel_id = alum_artifact_panel_serializer.data['id']
                            alum_panel_section={}
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0192').id # traslape
                            alum_panel_section['length'] = panel_new['height']
                            alum_panel_section['amount'] = 1
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0192').name
                            alum_panel_section['artifact_panel_id'] = artifact_panel_id
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections enganche
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0147').id # enganche
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0147').name
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections zocalo
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0349').id # zocalo
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0349').name
                            alum_panel_section['length'] = (float(data['width'])-2.5)/3
                            alum_panel_section['amount'] = 2
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            
                if panels_o_count > 0:   #  FIJOS
                    string_index = 0
                    for i in range(panels_o_count):
                        print('i: ', i)
                        print('design: ', design)
                        string_index = design.index('O',i if i == 0 else string_index+1)
                        print('string_index: ', string_index)
                        panel_new['position'] = string_index + 1
                        panel_new['amount_panel'] = panels_x_count
                        panel_new['panel_type'] = PANEL_TYPE[1][0]
                        print('panel_new: ', panel_new)
                        if design in ['OX','XO']:
                            panel_new['width'] =  (float(data['width']))/2
                            panel_new['height'] = float(data['height'])-2.6
                            alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                            alum_artifact_panel_serializer.is_valid(raise_exception=True)
                            alum_artifact_panel_serializer.save()
                            artifact_panel_id = alum_artifact_panel_serializer.data['id']
                            # panel sections traslape 
                            alum_panel_section={}
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0192').id # traslape
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0192').name
                            alum_panel_section['length'] = panel_new['height']
                            alum_panel_section['amount'] = 1
                            alum_panel_section['artifact_panel_id'] = artifact_panel_id
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections enganche
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0147').id # enganche
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0147').name
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections zocalo
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0349').id # zocalo
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0349').name
                            alum_panel_section['length'] = (float(data['width'])-2.5)/2
                            alum_panel_section['amount'] = 2
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                        if design in['XOX']:
                            panel_new['width'] =  (float(data['width']))/4*2
                            panel_new['height'] = float(data['height'])-2.6
                            alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                            alum_artifact_panel_serializer.is_valid(raise_exception=True)
                            alum_artifact_panel_serializer.save()
                            artifact_panel_id = alum_artifact_panel_serializer.data['id']
                            alum_panel_section={}
                            
                            """ 
                            Este fijo no tiene traslape, solo enganche y zocalo
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0192').id if panel_new['position'] == 1\
                                else AlumSection.objects.get(sku='ALN0147').id # traslape o enganche según sea el caso
                            alum_panel_section['length'] = panel_new['height']
                            alum_panel_section['amount'] = 1
                            alum_panel_section['artifact_panel_id'] = artifact_panel_id
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save() """
                            # panel sections enganche
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0147').id # enganche
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0147').name
                            alum_panel_section['length'] = panel_new['height']
                            alum_panel_section['amount'] = 2
                            alum_panel_section['artifact_panel_id'] = artifact_panel_id
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections zocalo
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0349').id # zocalo
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0349').name
                            alum_panel_section['length'] = (float(data['width'])/4)*2
                            alum_panel_section['amount'] = 2
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                        if design in ['OXXO']:
                            panel_new['width'] =  (float(data['width']))/4
                            panel_new['height'] = float(data['height'])-2.6
                            alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                            alum_artifact_panel_serializer.is_valid(raise_exception=True)
                            alum_artifact_panel_serializer.save()
                            artifact_panel_id = alum_artifact_panel_serializer.data['id']
                            alum_panel_section={}
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0192').id # traslape
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0192').name
                            alum_panel_section['length'] = panel_new['height']
                            alum_panel_section['amount'] = 1
                            alum_panel_section['artifact_panel_id'] = artifact_panel_id
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections enganche
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0147').id # enganche
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0147').name
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections zocalo
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0349').id # zocalo
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0349').name
                            alum_panel_section['length'] = (float(data['width'])-2.5)/4
                            alum_panel_section['amount'] = 2
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            
                if panels_p_count > 0:
                    string_index = 0
                    for i in range(panels_p_count):
                        string_index = design.index('P',i if i == 0 else string_index+1)
                        print('string_index: ', string_index)
                        panel_new['width'] =  (float(data['width'])/2)+1
                        panel_new['height'] = float(data['height'])-0.8
                        panel_new['position'] = string_index + 1
                        panel_new['amount_panel'] = panels_p_count
                        panel_new['panel_type'] = PANEL_TYPE[2][0]
                        
                        alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                        alum_artifact_panel_serializer.is_valid(raise_exception=True)
                        alum_artifact_panel_serializer.save()
                        artifact_panel_id = alum_artifact_panel_serializer.data['id']
                        if design in ['PXX','XXP']:
                            panel_new['width'] =  (float(data['width']))/3
                            panel_new['height'] = float(data['height'])-3.2
                            alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                            alum_artifact_panel_serializer.is_valid(raise_exception=True)
                            alum_artifact_panel_serializer.save()
                            artifact_panel_id = alum_artifact_panel_serializer.data['id']
                            # panel sections traslape 
                            alum_panel_section={}
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0192').id # traslape
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0192').name
                            alum_panel_section['length'] = panel_new['height']
                            alum_panel_section['amount'] = 1
                            alum_panel_section['artifact_panel_id'] = artifact_panel_id
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections enganche
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0147').id # enganche
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0147').name
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                            # panel sections zocalo
                            alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0349').id # zocalo
                            alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0349').name
                            alum_panel_section['length'] = (float(data['width'])-1)/2
                            alum_panel_section['amount'] = 2
                            alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                            alum_panel_section_serializer.is_valid(raise_exception=True)
                            alum_panel_section_serializer.save()
                        
                """ 
                    Marco de las 5020
                """
                panel_new['position']= 0
                panel_new['amount_panel'] = 1
                panel_new['panel_type'] = PANEL_TYPE[6][0]
                print('panel_new: ', panel_new)
                alum_artifact_panel_serializer = AlumArtifactPanelSerializer(data=panel_new)
                #print('alum_artifact_panel_serializer: ', alum_artifact_panel_serializer)
                alum_artifact_panel_serializer.is_valid(raise_exception=True)
                alum_artifact_panel_serializer.save()
                artifact_panel_id = alum_artifact_panel_serializer.data['id']
                # panel sections cabezal 
                alum_panel_section={}
                alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0144').id # cabezal
                alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0144').name
                alum_panel_section['length'] = data['width']
                alum_panel_section['amount'] = 1
                alum_panel_section['artifact_panel_id'] = artifact_panel_id
                alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                alum_panel_section_serializer.is_valid(raise_exception=True)
                alum_panel_section_serializer.save()
                # panel sections sillar
                alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0194').id # sillar
                alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0194').name
                alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                alum_panel_section_serializer.is_valid(raise_exception=True)
                alum_panel_section_serializer.save()
                # panel sections jamba
                alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0193').id # Jamba
                alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0193').name
                alum_panel_section['length'] = float(data['height'])-1.6
                alum_panel_section['amount'] = 2
                alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                alum_panel_section_serializer.is_valid(raise_exception=True)
                alum_panel_section_serializer.save()
                if data['has_alfajia']:
                    # panel sections alfajia
                    alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0612').id # alfajia
                    alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0612').name
                    alum_panel_section['length'] = float(data['width'])
                    alum_panel_section['amount'] = 1
                    alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                    alum_panel_section_serializer.is_valid(raise_exception=True)
                    alum_panel_section_serializer.save()
                # panel sections adaptador 5020
                if data['has_adapter']:
                    alum_panel_section['section_id'] = AlumSection.objects.get(sku='ALN0318').id # zocalo
                    alum_panel_section['name'] = AlumSection.objects.get(sku='ALN0318').name
                    alum_panel_section['length'] = panel_new['height']
                    alum_panel_section['amount'] = 1
                    alum_panel_section_serializer = AlumPanelSectionSerializer(data=alum_panel_section)
                    alum_panel_section_serializer.is_valid(raise_exception=True)
                    alum_panel_section_serializer.save()
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

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
              
    
        
