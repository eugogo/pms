# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MamCata(models.Model):
    id = models.ForeignKey('MamMaterial', models.DO_NOTHING, db_column='id', primary_key=True, related_name="cata_mat")
    cata_type = models.IntegerField()
    publish_state = models.IntegerField()
    delete_state = models.IntegerField()
    content_who = models.CharField(max_length=64, blank=True, null=True)
    content_where = models.CharField(max_length=64, blank=True, null=True)
    content_when = models.DateField(blank=True, null=True)
    content_what = models.CharField(max_length=64, blank=True, null=True)
    content_why = models.CharField(max_length=64, blank=True, null=True)
    shooting_user = models.CharField(max_length=64, blank=True, null=True)
    shooting_place = models.CharField(max_length=64, blank=True, null=True)
    shooting_date = models.DateField(blank=True, null=True)
    camera_position = models.CharField(max_length=64, blank=True, null=True)
    content_description = models.CharField(max_length=64, blank=True, null=True)
    video_rate = models.IntegerField(blank=True, null=True)
    video_format = models.CharField(max_length=64, blank=True, null=True)
    video_depth = models.IntegerField(blank=True, null=True)
    audio_rate = models.IntegerField(blank=True, null=True)
    audio_format = models.CharField(max_length=64, blank=True, null=True)
    audio_sample_rate = models.IntegerField(blank=True, null=True)
    audio_depth = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    create_description = models.CharField(max_length=512, blank=True, null=True)
    create_app = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mam_cata'


class MamCataExt(models.Model):
    id = models.BigAutoField(primary_key=True)
    cata = models.ForeignKey(MamCata, models.DO_NOTHING, related_name="ext_cata")
    attr_name = models.CharField(max_length=64)
    attr_value = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mam_cata_ext'


class MamFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    mat = models.ForeignKey('MamMaterial', models.DO_NOTHING, related_name="file_mat")
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    mam_type = models.IntegerField()
    ext_name = models.CharField(max_length=64)
    delete_state = models.IntegerField()
    publish_state = models.IntegerField()
    is_dir = models.IntegerField()
    loc_path = models.CharField(max_length=1024)
    file_size = models.BigIntegerField()
    file_md5 = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    create_type = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    create_app = models.CharField(max_length=64, blank=True, null=True)
    is_derived = models.IntegerField(blank=True, null=True)
    derive_type = models.IntegerField(blank=True, null=True)
    derive_template = models.CharField(max_length=64, blank=True, null=True)
    derive_from_ids = models.CharField(max_length=1024, blank=True, null=True)
    derive_description = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mam_file'


class MamMaterial(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    type = models.IntegerField()
    is_product = models.IntegerField()
    publish_state = models.IntegerField()
    cata_state = models.IntegerField()
    delete_state = models.IntegerField()
    duration = models.BigIntegerField(blank=True, null=True)
    frame_rate = models.IntegerField(blank=True, null=True)
    afd_value = models.CharField(max_length=64, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    audio_type = models.IntegerField(blank=True, null=True)
    channel_num = models.IntegerField(blank=True, null=True)
    version_code = models.CharField(max_length=64, blank=True, null=True)
    create_mode = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    create_description = models.CharField(max_length=512, blank=True, null=True)
    create_app = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    task_code = models.CharField(max_length=64, blank=True, null=True)
    owner_user = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mam_material'


class MamMaterialCheck(models.Model):
    id = models.BigAutoField(primary_key=True)
    mat = models.ForeignKey(MamMaterial, models.DO_NOTHING, related_name="check_mat")
    check_type = models.IntegerField()
    check_rule = models.CharField(max_length=64, blank=True, null=True)
    check_org = models.CharField(max_length=64, blank=True, null=True)
    check_state = models.IntegerField(blank=True, null=True)
    check_time = models.DateTimeField(blank=True, null=True)
    check_result = models.IntegerField(blank=True, null=True)
    check_decription = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mam_material_check'


class MamMatgroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    type = models.IntegerField(default=0)
    delete_state = models.IntegerField(default=0)
    publish_state = models.IntegerField(default=0)

    # materials = models.ManyToManyField(MamMaterial, through='MamMatgroupMat', through_fields=('group', 'mat'))


    class Meta:
        managed = False
        db_table = 'mam_matgroup'


class MamMatgroupMat(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(MamMatgroup, models.DO_NOTHING, blank=True, null=True)
    mat = models.ForeignKey(MamMaterial, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mam_matgroup_mat'


class MamMatgroupTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    matg = models.ForeignKey(MamMatgroup, models.DO_NOTHING, related_name="task_matg")
    task_code = models.CharField(max_length=64)
    is_readable = models.IntegerField()
    is_writable = models.IntegerField()
    is_deletable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mam_matgroup_task'


class MamMatgroupUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    matg = models.ForeignKey(MamMatgroup, models.DO_NOTHING, related_name="user_matg")
    user_code = models.CharField(max_length=64)
    is_readable = models.IntegerField()
    is_writable = models.IntegerField()
    is_deletable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mam_matgroup_user'


class MamScene(models.Model):
    id = models.BigAutoField(primary_key=True)
    mat = models.ForeignKey(MamMaterial, models.DO_NOTHING, related_name="scene_mat")
    in_point = models.CharField(max_length=32)
    out_point = models.CharField(max_length=32)
    description = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'mam_scene'
