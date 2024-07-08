from abc import ABC, abstractmethod
from typing import Dict, List, Any

class IAlumArtifactService(ABC):
    @abstractmethod
    def create_alum_artifact(self, data: Dict[str, Any]) -> Dict[str, Any]:
        pass

class IAlumSystemService(ABC):
    @abstractmethod
    def get_all(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def get_by_name(self, name: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def create_alum_system(self, data: Dict[str, Any]) -> Dict[str, Any]:
        pass
