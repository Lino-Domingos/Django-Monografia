# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AscKamavota(models.Model):
    geom = models.MultiPolygonField(dim=3, blank=True, null=True)
    oid_field = models.BigIntegerField(db_column='oid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    name = models.CharField(max_length=254, blank=True, null=True)
    folderpath = models.CharField(max_length=254, blank=True, null=True)
    symbolid = models.BigIntegerField(blank=True, null=True)
    altmode = models.BigIntegerField(blank=True, null=True)
    base = models.FloatField(blank=True, null=True)
    clamped = models.BigIntegerField(blank=True, null=True)
    extruded = models.BigIntegerField(blank=True, null=True)
    snippet = models.CharField(max_length=254, blank=True, null=True)
    popupinfo = models.CharField(max_length=254, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ASC- Kamavota'


class AccountsAsc(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    codigo_asc = models.CharField(db_column='codigo_ASC', max_length=2)  # Field name made lowercase.
    direccao_regional = models.ForeignKey('AccountsDireccaoRegional', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_asc'


class AccountsDireccaoRegional(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_direccao = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.ForeignKey('AccountsProvincia', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Accounts_direccao_regional'


class AccountsProvincia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_provincia = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Accounts_provincia'


class AccountsUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    user_type = models.CharField(max_length=20)
    asc = models.ForeignKey(AccountsAsc, models.DO_NOTHING, db_column='ASC_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Accounts_user'


class AccountsUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_user_groups'
        unique_together = (('user', 'group'),)


class AccountsUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_user_user_permissions'
        unique_together = (('user', 'permission'),)


class PostoDeTransformao(models.Model):
    geom = models.PointField(blank=True, null=True)
    id_0 = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    pt_number = models.CharField(db_column='PT NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    latittude = models.FloatField(db_column='Latittude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Posto de Transformação '


class ProjectLvFeeder(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'Project_lv_feeder'


class ProjectLvFeederPt(models.Model):
    id = models.BigAutoField(primary_key=True)
    lv_feeder = models.ForeignKey(ProjectLvFeeder, models.DO_NOTHING)
    pt = models.ForeignKey('ProjectPt', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Project_lv_feeder_PT'
        unique_together = (('lv_feeder', 'pt'),)


class ProjectProjectType(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'Project_project_type'


class ProjectProjecto(models.Model):
    id = models.BigAutoField(primary_key=True)
    lv = models.ForeignKey(ProjectLvFeeder, models.DO_NOTHING, db_column='LV_id')  # Field name made lowercase.
    equipe = models.ForeignKey('TeamTeam', models.DO_NOTHING)
    tipo = models.ForeignKey(ProjectProjectType, models.DO_NOTHING)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Project_projecto'


class ProjectPt(models.Model):
    id = models.BigAutoField(primary_key=True)
    pt_number = models.CharField(db_column='PT_NUMBER', max_length=20)  # Field name made lowercase.
    asc = models.ForeignKey(AccountsAsc, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Project_pt'


class TaskTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    project = models.ForeignKey(ProjectProjecto, models.DO_NOTHING)
    acess_denied = models.IntegerField()
    meter_box = models.IntegerField()
    premisses_locked = models.IntegerField(db_column='premisses_Locked')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Task_task'


class TeamTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    state = models.BooleanField()
    date_created = models.DateTimeField()
    asc = models.ForeignKey(AccountsAsc, models.DO_NOTHING)
    creator = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    supervisor = models.ForeignKey(AccountsUser, models.DO_NOTHING, related_name='teamteam_supervisor_set')
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Team_team'


class TeamTeamMembros(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.ForeignKey(TeamTeam, models.DO_NOTHING)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Team_team_membros'
        unique_together = (('team', 'user'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
