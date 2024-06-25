from rest_framework import routers
from main_app.api.view.alum_system_view import AlumSystemDescriptionViewSet
from main_app.views import (AlumSystemViewSet, AlumLineViewSet, AlumSectionViewSet, AlumArtifactViewSet, AlumArtifactPanelViewSet)

router = routers.SimpleRouter()

router.register(r'alumsystem', AlumSystemViewSet, basename='alumsystem')
router.register(r'alumsystem/<int:pk>/alumsystemdescription', AlumSystemDescriptionViewSet, basename='alumsystemdescription')
router.register(r'alumsystemdescription', AlumSystemDescriptionViewSet, basename='alumsystemdescription-5')
router.register(r'alumline', AlumLineViewSet, basename='alumline')
router.register(r'alumsection', AlumSectionViewSet, basename='alumsection')
router.register(r'alumartifact', AlumArtifactViewSet, basename='alumartifact')
router.register(r'alumartifactpanel', AlumArtifactPanelViewSet, basename='alumartifactpanel')


# router.register(r'users', UserViewSet)
# router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls

