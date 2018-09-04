# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StorAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_remote = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    acc_cert = models.CharField(max_length=512, blank=True, null=True)
    home_dir = models.CharField(max_length=1024, blank=True, null=True)
    quota_size = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_type = models.IntegerField(blank=True, null=True)
    create_user = models.BigIntegerField(blank=True, null=True)
    storage = models.ForeignKey('StorStorage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stor_account'


class StorAccountPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    workspace = models.ForeignKey('StorWorkspace', models.DO_NOTHING)
    account = models.ForeignKey(StorAccount, models.DO_NOTHING)
    permission = models.ForeignKey('StorPermission', models.DO_NOTHING)
    expire_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stor_account_permission'


class StorGroup(models.Model):
    id = models.ForeignKey(StorAccount, models.DO_NOTHING, db_column='id', primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    type = models.IntegerField()
    group_gid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stor_group'


class StorGroupUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey(StorGroup, models.DO_NOTHING)
    user = models.ForeignKey('StorUser', models.DO_NOTHING)
    join_state = models.IntegerField()
    join_time = models.DateTimeField(blank=True, null=True)
    group_role = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stor_group_user'


class StorPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    is_active = models.IntegerField()
    is_deleted = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    create_time = models.DateTimeField()
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stor_permission'


class StorStorage(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    host_ip = models.CharField(max_length=64)
    host_name = models.CharField(max_length=64)
    is_disable = models.IntegerField()
    is_deleted = models.IntegerField()
    capacity = models.BigIntegerField()
    share_path = models.CharField(max_length=64, blank=True, null=True)
    share_name = models.CharField(max_length=64, blank=True, null=True)
    is_isolated = models.IntegerField(blank=True, null=True)
    is_editable = models.IntegerField(blank=True, null=True)
    dir_level = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stor_storage'


class StorUser(models.Model):
    id = models.ForeignKey(StorAccount, models.DO_NOTHING, db_column='id', primary_key=True)
    user_uid = models.CharField(max_length=64, blank=True, null=True)
    pwd = models.CharField(max_length=64)
    type = models.IntegerField()
    priority_limit = models.IntegerField(blank=True, null=True)
    bandwith_limit = models.IntegerField(blank=True, null=True)
    privilage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stor_user'


class StorWorkspace(models.Model):
    id = models.BigAutoField(primary_key=True)
    storage = models.ForeignKey(StorStorage, models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    type = models.IntegerField()
    is_active = models.IntegerField()
    is_deleted = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    quota_type = models.IntegerField(blank=True, null=True)
    quota_size = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    service_for = models.CharField(max_length=64, blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_rule = models.CharField(max_length=64, blank=True, null=True)
    create_app = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stor_workspace'
