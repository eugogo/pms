# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UumAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('UumUser', models.DO_NOTHING)
    nation = models.CharField(max_length=128)
    province = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    postcode = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'uum_address'


class UumGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)
    type = models.IntegerField()
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    img_url = models.CharField(max_length=2048, blank=True, null=True)
    create_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    description = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uum_group'


class UumGroupUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(UumGroup, models.DO_NOTHING)
    user = models.ForeignKey('UumUser', models.DO_NOTHING)
    remark = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uum_group_user'
        unique_together = (('group', 'user'),)


class UumImg(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    ownkey = models.BigIntegerField(blank=True, null=True)
    path = models.CharField(max_length=2048)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uum_img'


class UumPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)
    type = models.IntegerField()
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    page_url = models.CharField(max_length=1024, blank=True, null=True)
    img_url = models.CharField(max_length=2048, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uum_permission'


class UumRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    img_url = models.CharField(max_length=2048, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uum_role'


class UumRolePermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    perm = models.ForeignKey(UumPermission, models.DO_NOTHING)
    role = models.ForeignKey(UumRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'uum_role_permission'


class UumUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=64)
    type = models.IntegerField()
    password = models.CharField(max_length=64)
    mail = models.CharField(unique=True, max_length=64, blank=True, null=True)
    mobile = models.CharField(unique=True, max_length=16, blank=True, null=True)
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    create_time = models.DateTimeField()
    create_type = models.IntegerField()
    rank_level = models.IntegerField()
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    default_img = models.CharField(max_length=2048, blank=True, null=True)
    invite_code = models.CharField(max_length=64, blank=True, null=True)
    duty_title = models.CharField(max_length=16, blank=True, null=True)
    office_phone = models.CharField(max_length=16, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    political_status = models.CharField(max_length=64, blank=True, null=True)
    default_address = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uum_user'


class UumUserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UumUser, models.DO_NOTHING)
    role = models.ForeignKey(UumRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'uum_user_role'
        unique_together = (('user', 'role'),)
