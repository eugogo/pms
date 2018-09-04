from mam.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from utils.utils import format


@csrf_exempt
def load_matgroups(request, pageIndex=None, pageSize=None):
    objs = MamMatgroup.objects.all();
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


def get_group_by_id(request, id):
    objs = MamMatgroup.objects.filter(id=id)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


def load_matgroups_by_user_code(request, user_code, pageIndex=None, pageSize=None):
    objs = MamMatgroup.objects.filter(user_matg__user_code=user_code)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)


def load_matgroups_by_task_code(request, task_code, pageIndex=None, pageSize=None):
    objs = MamMatgroup.objects.filter(task_matg__task_code=task_code)
    data = format.formatResponsePageLoad(objs)
    return JsonResponse(data)

