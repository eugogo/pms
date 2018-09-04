from mam.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from utils.utils import format


# 所有素材
def load_matirials(request, pageIndex=None, pageSize=None):
    objs = MamMaterial.objects.all();
    data = format.formatResponsePageLoad(objs, pageIndex, pageSize)
    print("()()(()()()()()()()(")
    print(data)
    return JsonResponse(data)


# 指定id素材
def load_materials_by_id(request, mat_id, pageIndex=None, pageSize=None):
    objs = MamMaterial.objects.filter(id=mat_id)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


# 指定分组的所有素材
def load_materials_by_group_id(request, group_id, pageIndex=None, pageSize=None):
    objs = MamMatgroup.objects.filter(id=group_id).first().material_set.all()
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


# 指定用户[拥有]的所有素材，传递用户代码，需为字母和数字
def load_materials_by_usercode(request, user_code, pageIndex=None, pageSize=None):
    # groups = MamMatgroup.objects.filter(user_matg__user_code=user_code)
    objs = MamMaterial.objects.filter(owner_user=user_code)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


# 指定task的所有素材，传递栏目代码，需为字母和数字
def load_materials_by_task_code(request, task_code, pageIndex=None, pageSize=None):
    objs = MamMaterial.objects.filter(task_code=task_code)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


# 指定编目项的所有素材
def load_materials_by_cata(request, pageIndex=None, pageSize=None):
    cata_mat = None
    objs = MamMaterial.objects.filter(cata_mat=cata_mat)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


# 指定素材属性的所有素材
def load_materials_by_material(request, pageIndex=None, pageSize=None):
    material = None
    objs = MamMaterial.objects.filter(material=material)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


