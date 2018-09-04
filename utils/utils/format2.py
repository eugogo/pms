
from django.core import serializers
from django.core.paginator import Paginator
import json
from collections import Iterable
# from task.serializer.task_serializer import TaskSerializer


import logging

logger = logging.getLogger("django")


# def formatResponseGet(objs):
#     response_data = {}
#     response_data['resultCode'] = 0
#     response_data['resultMsg'] = "success"
#     resultData = []
#     if isinstance(objs, Iterable):
#         # response_data['resultData'] = serializers.serialize('json', object)
#         for obj in objs:
#             task = TaskSerializer(obj)
#             resultData.append(task.data)
#     else:
#         # response_data['resultData'] = json.dump(objs)
#         task = TaskSerializer(objs)
#         resultData.append(task.data)
#
#     response_data['resultData'] = resultData
#
#     return response_data
#




#
#
def formatResponsePageLoad(list, pageIndex=1, pageSize=50):
    if list is None:
        raise ValueError("list param should not be none!")


    pageInfo = None
    resultData = None

    if pageIndex is None or pageSize is None:
        resultData = serializers.serialize('json', list)
        return fomatResponse(resultData, pageInfo)

    else:
        # raise ValueError("error param for pageIndex or pageSize. it should be positive integer。")
        resultData = pageLoad(list, pageIndex, pageSize)
        if (resultData is not None):
            pageInfo = formatPageInfo(len(list), pageIndex, pageSize)
        return fomatResponse(resultData, pageInfo)




def fomatResponse(resultData, pageInfo=None):
    response_data = {}
    response_data['resultCode'] = 0
    response_data['resultMsg'] = 'success'

    if resultData is None:
        response_data['resultMsg'] = 'nothing to load!'
    else:
        response_data['pageInfo'] = pageInfo
        response_data['resultData'] = resultData

    return response_data




def formatPageInfo(totalCount, pageIndex, pageSize):
    pageInfo = {}
    pageInfo['pageIndex'] = pageIndex
    pageInfo['pageSize'] = pageSize
    pageInfo['totalCount'] = totalCount
    # 总页数
    totalPage = totalCount // pageSize
    if totalCount % pageSize > 0:
        totalPage += 1
    pageInfo['totalPage'] = totalPage
    return pageInfo


def pageLoad(list, pageIndex, pageSize):
    resultData = None

    if pageIndex > 0 and pageSize > 0:

        # 将信息按每页显示的条数进行分页
        p = Paginator(list, pageSize)

        # 获取第pageIndex页的数据
        list2 = p.page(pageIndex)
        if(len(list2) > 0):
            resultData = serializers.serialize('json', list2)
    else:
        resultData = serializers.serialize('json', list)


    # logger.debug("resultData json data --> %s" % resultData)
    print("resultData json data --> %s" % resultData)

    return resultData


