from django.conf.urls import url
from mam.views import cata_views, check_views, file_views, material_views,matgroup_views




urlpatterns = [

    #-----------------------#
    #------matgroups--------#

    # 所有分组
    url(r'^matgroups/$', matgroup_views.load_matgroups),

    # 指定id的分组
    url(r'^matgroups/(\d+)/$', matgroup_views.get_group_by_id),

    # 指定用户的所有分组，传递用户代码，需为字母和数字
    url(r'^matgroups/users/(\w+)/$', matgroup_views.load_matgroups_by_user_code),

    # 指定task的所有分组，传递栏目代码，需为字母和数字
    url(r'^matgroups/tasks/(\w+)/$', matgroup_views.load_matgroups_by_task_code),


    #------materials--------#
    #-----------------------#

    # 所有素材
    url(r'^materials/$', material_views.load_matirials),
    url(r'^materials/(?P<pageIndex>\d+)/(?P<pageSize>\d+)/$', material_views.load_matirials),

    # 指定id素材
    url(r'^materials/(\d+)/$', material_views.load_materials_by_id),
    url(r'^materials/(\d+)/(?P<pageIndex>\d+)/(?P<pageSize>\d+)/$', material_views.load_materials_by_id),

    # 指定分组的所有素材
    url(r'^materials/matgroups/(\d+)/$', material_views.load_materials_by_group_id),
    url(r'^materials/matgroups/(\d+)/(?P<pageIndex>\d+)/(?P<pageSize>\d+)/$', material_views.load_materials_by_group_id),

    # 指定用户的所有素材，传递用户代码，需为字母和数字
    url(r'^materials/users/(\w+)/$', material_views.load_materials_by_usercode),
    url(r'^materials/users/(\w+)/(?P<pageIndex>\d+)/(?P<pageSize>\d+)/$', material_views.load_materials_by_usercode),

    # 指定task的所有素材，传递栏目代码，需为字母和数字
    url(r'^materials/tasks/(\w+)/$', material_views.load_materials_by_task_code),
    url(r'^materials/tasks/(\w+)/(?P<pageIndex>\d+)/(?P<pageSize>\d+)/$', material_views.load_materials_by_task_code),

     # 指定编目项的所有素材
    url(r'^materials/catas/$', material_views.load_materials_by_cata),

     # 指定素材属性的所有素材
    url(r'^materials/materials/$', material_views.load_materials_by_material),



    #--------cata----------#
    #----------------------#

    # 指定素材的所有场景，传递栏目代码，需数字
    url(r'^scenes/materials/(\d+)/$', cata_views.load_scenes_by_material_id),
    url(r'^scenes/materials/(\d+)/(?P<pageIndex>\d+)/(?P<pageSize>\d+)/$', cata_views.load_scenes_by_material_id),

    # 指定素材的编目信息（含扩展集），传递栏目代码，数字
    url(r'^catas/materials/(\d+)/$', cata_views.get_cata_by_material_id),



    #--------check----------#
    #-----------------------#

    # 指定素材的所有场景，传递栏目代码，需数字
    url(r'^checks/materials/(\d+)/$', cata_views.load_scenes_by_material_id),



    #--------file----------#
    #----------------------#

    # 指定素材的所有文件
    url(r'^files/materials/(\d+)/$', file_views.load_files_by_material_id),
    url(r'^files/materials/(\d+)/(?P<pageIndex>\d+)/(?P<pageSize>\d+)/$', file_views.load_files_by_material_id),

    # url(r'^items/(?P<id>\w+)/$',view.op_item),
]


