from .interfaces import IAlumSystemService
from main_app.model.alum_system import AlumSystem

class AlumSystemService(IAlumSystemService):

    def get_all(self):
        alum_systems = AlumSystem.objects.all()
        return alum_systems

    def get_by_id(self, id: int):
        alum_system = AlumSystem.objects.get(id=id)
        return alum_system
        
    def get_by_name(self, name: str):
        try:
            alum_system = AlumSystem.objects.filter(name=name).first()
            return alum_system
        except AlumSystem.DoesNotExist:
            return None
        

    def create_alum_system(self, data: dict):
        alum_system = AlumSystem.objects.create(**data)
        return alum_system
        
        