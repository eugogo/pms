# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TaskAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    task = models.ForeignKey('TaskInfo', models.DO_NOTHING)
    code = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    work_hours = models.IntegerField(blank=True, null=True)
    assign_mode = models.IntegerField(blank=True, null=True)
    workers = models.CharField(max_length=64)
    res_type = models.IntegerField()
    res_code = models.CharField(max_length=64)
    is_published = models.IntegerField()
    is_confirmed = models.IntegerField()
    confirm_user = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    max_confirm_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_assign'


class TaskAssignConfirm(models.Model):
    id = models.BigAutoField(primary_key=True)
    assign = models.ForeignKey(TaskAssign, models.DO_NOTHING)
    code = models.CharField(max_length=64)
    confirm_no = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    work_hours = models.IntegerField()
    quality_level = models.IntegerField()
    efficiency_level = models.IntegerField()
    friendliness_level = models.IntegerField()
    description = models.CharField(max_length=1024, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_assign_confirm'


class TaskChange(models.Model):
    id = models.BigIntegerField(primary_key=True)
    task = models.ForeignKey('TaskInfo', models.DO_NOTHING)
    change_code = models.CharField(max_length=80)
    change_time = models.DateTimeField()
    change_user = models.CharField(max_length=64)
    change_no = models.IntegerField()
    work_load = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    change_reason = models.CharField(max_length=1024)
    change_state = models.IntegerField()
    check_time = models.DateTimeField(blank=True, null=True)
    check_state = models.IntegerField(blank=True, null=True)
    check_result = models.IntegerField(blank=True, null=True)
    check_description = models.CharField(max_length=1024, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_change'


class TaskConfirm(models.Model):
    id = models.ForeignKey('TaskInfo', models.DO_NOTHING, db_column='id', primary_key=True)
    code = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    work_hours = models.IntegerField()
    quality_level = models.IntegerField()
    efficiency_level = models.IntegerField()
    friendliness_level = models.IntegerField()
    description = models.CharField(max_length=1024, blank=True, null=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    check_time = models.DateTimeField(blank=True, null=True)
    check_state = models.IntegerField(blank=True, null=True)
    check_result = models.IntegerField(blank=True, null=True)
    check_description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_confirm'


class TaskGroup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    type = models.IntegerField()
    publish_state = models.IntegerField()
    delete_state = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_group'


class TaskGroupTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(TaskGroup, models.DO_NOTHING)
    task = models.ForeignKey('TaskInfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'task_group_task'


class TaskInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=64)
    type = models.IntegerField()
    sub_type = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField()
    exec_state = models.IntegerField()
    is_deleted = models.IntegerField()
    is_cancel = models.IntegerField(blank=True, null=True)
    publish_state = models.IntegerField()
    max_chan_no = models.IntegerField()
    confirm_state = models.IntegerField()
    manager = models.CharField(max_length=64, blank=True, null=True)
    cc_users = models.CharField(max_length=1024, blank=True, null=True)
    confirm_user = models.CharField(max_length=64, blank=True, null=True)
    column_code = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    create_type = models.CharField(max_length=64, blank=True, null=True)
    create_app = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_info'


class TaskMaterial(models.Model):
    id = models.BigAutoField(primary_key=True)
    task = models.ForeignKey(TaskInfo, models.DO_NOTHING)
    mat_code = models.CharField(max_length=64)
    is_readable = models.IntegerField()
    is_writable = models.IntegerField()
    is_deletable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task_material'


class TaskRequirement(models.Model):
    id = models.BigAutoField(primary_key=True)
    task = models.ForeignKey(TaskInfo, models.DO_NOTHING)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    req_content = models.CharField(max_length=256)
    status = models.IntegerField()
    type = models.IntegerField()
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_requirement'


class TaskTrack(models.Model):
    id = models.ForeignKey(TaskInfo, models.DO_NOTHING, db_column='id', primary_key=True)
    task_id = models.BigIntegerField()
    tack_type = models.IntegerField(blank=True, null=True)
    track_user = models.CharField(max_length=64)
    track_time = models.DateTimeField()
    is_backend = models.IntegerField(blank=True, null=True)
    track_content = models.CharField(max_length=1024)
    is_deleted = models.IntegerField(blank=True, null=True)
    task_progress = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_track'
