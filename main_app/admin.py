from django.contrib import admin

from .models import (AlumSystem, AlumLine, AlumSection, AlumLineDescription, 
                    AlumSystemDescription, AlumSectionDescription, AlumSectionMeasure, 
                    AlumPanelSection, AlumArtifact, AlumArtifactPanel)

# Register your models here.

admin.site.register(AlumSystem)
admin.site.register(AlumLine)
admin.site.register(AlumSection)
admin.site.register(AlumLineDescription)
admin.site.register(AlumSystemDescription)
admin.site.register(AlumSectionDescription)
admin.site.register(AlumSectionMeasure)
admin.site.register(AlumPanelSection)
admin.site.register(AlumArtifact)
admin.site.register(AlumArtifactPanel)






