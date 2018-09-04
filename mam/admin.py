from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your model here.
from django.contrib import admin
from .models import *


admin.site.register(MamCata)
admin.site.register(MamFile)
admin.site.register(MamMaterial)
admin.site.register(MamMatgroup)
admin.site.register(MamMatgroupTask)
admin.site.register(MamMatgroupMat)
admin.site.register(MamMatgroupUser)
admin.site.register(MamScene)
admin.site.register(MamMaterialCheck)

