# import logging
#
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from uum.models import UumUser
# from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
# from django.http import JsonResponse
# from uum.serializer import user_serializer
# import json
#
#
# logger = logging.getLogger('django')
#
# # Create your view here.
# @api_view(['GET','POST','PUT'])
# @csrf_exempt
# def load(request):
#     # data = ({"hello":"test"},{"hello1":"test1"})
#     data = UumUser.objects.filter().values("user_name","user_id","user_type")
#     print("data--%s" % data)
#     return Response(data)
#
#
#
#
#
# @api_view(['POST', 'GET'],)
# @csrf_exempt
# def login(request, id, password):
#     method = request.method
#     data = 'ok'
#     if method == 'GET':
#         try:
#             user = UumUser.objects.get(id=id, password=password)
#             logger.debug('task --> %s' % user)
#         except:
#             data = "用户名不存在或者用户名密码不匹配"
#     elif method == 'POST':
#         pass
#
#     return JsonResponse(format.formatResponseGet(data))
#
#
#
#
# @api_view(['POST'])
# @csrf_exempt
# def create(request):
#     data = json.loads(request.body.decode(encoding='utf-8'))
#     user = serializers.deserialize("json", data)
#
#     serializer = user_serializer.TaskSerializer(data=data)
#     if serializer.is_valid(data):
#         # task = serializer.create_or_updata(data)
#         task = serializer.create(data)
#         print("task id -- > %s" % task.task_id)
#         task_ids.append(task.task_id)
#
#
# @api_view(['GET'])
# @csrf_exempt
# def loginSuccess(request, id):
#     task = UumUser.objects.filter(task_id=id)
#
#     logger.debug('task --> %s' % task)
#
#     return JsonResponse(format.formatResponseGet(task))
#
#
#
#
# @api_view(['GET'])
# @csrf_exempt
# def logout(request, id):
#     task = UumUser.objects.filter(task_id=id)
#
#     logger.debug('task --> %s' % task)
#
#     return JsonResponse(format.formatResponseGet(task))
#
#
#
# @api_view(['GET'])
# @csrf_exempt
# def getUser(request, id):
#     task = UumUser.objects.filter(task_id=id)
#
#     logger.debug('task --> %s' % task)
#
#     return JsonResponse(format.formatResponseGet(task))
#
#
# @csrf_exempt
# def getTaskWithDetail(request, taskId):
#     task = UumUser.objects.filter(task_id=taskId)
#     logger.debug('task --> %s' % task)
#
#     return JsonResponse(format.formatResponseGet(task))
#
#
#
