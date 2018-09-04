from mam.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from utils.utils import format

def load_scenes_by_material_id(request, mat_id, pageIndex=None, pageSize=None):
    objs = MamScene.objects.filter(mat_id=mat_id)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


def get_cata_by_material_id(request, mat_id):
    objs = MamCata.objects.filter(id=mat_id)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)
