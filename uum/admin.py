from django.contrib import admin

# Register your model here.
from django.contrib import admin
from .models import *


admin.site.register(UumUser)
admin.site.register(UumPermission)
admin.site.register(UumGroup)
admin.site.register(UumRole)
admin.site.register(UumGroupUser)
admin.site.register(UumRolePermission)
admin.site.register(UumUserRole)
admin.site.register(UumImg)
admin.site.register(UumAddress)
