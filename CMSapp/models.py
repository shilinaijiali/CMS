from django.db import models
from django.utils.translation import gettext_lazy as _


class ConsumableType(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=40)
    comment = models.CharField(verbose_name=_('comment'), max_length=500, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True)
    lastupdate = models.DateTimeField(verbose_name=_('lastupdate'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name",)
        verbose_name = _('ConsumableTypeGroup')
        verbose_name_plural = verbose_name
        db_table = 'ConsumableTypeGroup'


class TypeGroup(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=40)
    ConsumableType = models.ForeignKey(ConsumableType, verbose_name=_('ConsumableType'), on_delete=models.CASCADE)
    comment = models.CharField(verbose_name=_('comment'), max_length=500, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True)
    lastupdate = models.DateTimeField(verbose_name=_('lastupdate'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "ConsumableType")
        verbose_name = _('TypeGroup')
        verbose_name_plural = verbose_name
        db_table = 'TypeGroup'


class TypeDefinition(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=40)
    typegroup = models.ForeignKey(TypeGroup, verbose_name=_('typegroup'), on_delete=models.CASCADE)
    comment = models.CharField(verbose_name=_('comment'), max_length=500, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True)
    lastupdate = models.DateTimeField(verbose_name=_('lastupdate'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "typegroup")
        verbose_name = _('TypeDefinition')
        verbose_name_plural = verbose_name
        db_table = 'TypeDefinition'


class Consumable(models.Model):
    sn = models.CharField(verbose_name=_('Sn'), max_length=40, unique=True, primary_key=True)
    entertime = models.DateTimeField(auto_now_add=False, verbose_name=_('entertime'))
    # limit_choices_to={'typegroup__name': 'VersionType'}：将admin中version外键的取值范围定为TypeDenfinition表中name为VersionType的值
    version = models.ForeignKey(TypeDefinition, verbose_name=_('version'), on_delete=models.CASCADE, related_name='version', limit_choices_to={'typegroup__name__endswith': 'Version'})
    tooltype = models.ForeignKey(TypeDefinition, verbose_name=_('ToolType'), on_delete=models.CASCADE, related_name='tooltype', limit_choices_to={'typegroup__name__endswith': 'Type'})
    model = models.ForeignKey(TypeDefinition, verbose_name=_('Model'), on_delete=models.CASCADE, related_name='model', limit_choices_to={'typegroup__name__endswith': 'Model'})
    status = models.CharField(verbose_name=_('Status'), max_length=40, default='Stock')
    usefullife = models.IntegerField(verbose_name=_('Usefullife'), default=0)
    ratedlife = models.IntegerField(verbose_name=_('Ratedlife'), default=0)
    location = models.CharField(verbose_name=_('Location'), max_length=40, null=True, blank=True)
    position = models.CharField(verbose_name=_('Position'), max_length=40, null=True, blank=True)
    createtime = models.DateTimeField(auto_now_add=True)
    updateuser = models.CharField(max_length=40)
    updatetime = models.DateTimeField(auto_now=True)
    comment = models.CharField(verbose_name=_('Comment'), max_length=200, null=True, blank=True)
    inscrapping = models.BooleanField(verbose_name='inscrapping', default=False)
    pkg = models.BooleanField(verbose_name=_('pkg'), default=True)
    mark = models.BooleanField(verbose_name=_('mark'), default=True)
    OQC = models.BooleanField(verbose_name=_('OQC'), default=True)
    appearance = models.BooleanField(verbose_name=_('appearance'), default=True)
    EmulsionShedding = models.BooleanField(verbose_name=_('EmulsionShedding'), default=True)
    MeshPlugging = models.BooleanField(verbose_name=_('MeshPlugging'), default=True)
    ConsumableType = models.ForeignKey(ConsumableType, verbose_name=_('ConsumableType'), on_delete=models.CASCADE, related_name='ConsumableType')

    class Meta:
        verbose_name = _('Consumable')
        verbose_name_plural = verbose_name
        db_table = 'Consumable'
        # abstract = True   # 新增栏位重新迁移数据库报错时解决方案


class MouldsUseHistory(models.Model):
    sn = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    version = models.CharField(max_length=40)
    tooltype = models.CharField(max_length=40)
    usetime = models.CharField(max_length=40)
    usenumber = models.IntegerField(default=0)
    position = models.CharField(max_length=40)
    updatetime = models.DateTimeField(auto_now=True)
    updateuser = models.CharField(max_length=40)
    comment = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'MouldsUseHistory'


class ScreenUseHistory(models.Model):
    sn = models.CharField(max_length=40)
    CheckTime = models.DateTimeField(verbose_name=_('CheckTime'), auto_now_add=True)
    X1 = models.FloatField(default=0)
    X2 = models.FloatField(default=0)
    Y1 = models.FloatField(default=0)
    Y2 = models.FloatField(default=0)
    Z1 = models.FloatField(default=0)
    Z2 = models.FloatField(default=0)
    P1 = models.FloatField(default=0)
    P2 = models.FloatField(default=0)
    P3 = models.FloatField(default=0)
    P4 = models.FloatField(default=0)
    P5 = models.FloatField(default=0)
    P6 = models.FloatField(default=0)
    P7 = models.FloatField(default=0)
    P8 = models.FloatField(default=0)
    P9 = models.FloatField(default=0)
    EmulsionShedding = models.BooleanField(verbose_name=_('EmulsionShedding'), default=True)
    MeshPlugging = models.BooleanField(verbose_name=_('MeshPlugging'), default=True)
    CheckOperator = models.CharField(verbose_name=_('CheckOperator'), max_length=40, null=True, blank=True)
    PrintingNumber = models.IntegerField(verbose_name=_('PrintingNumber'), default=0, null=True, blank=True)
    Print_Operator = models.CharField(verbose_name=_('Use_Operator'), max_length=40, null=True, blank=True)
    AddUpPrint = models.IntegerField(verbose_name=_('AddUpPrint'), default=0, null=True, blank=True)
    Add_Operator = models.CharField(verbose_name=_('Add_Operator'), max_length=40, null=True, blank=True)
    Clean = models.BooleanField(verbose_name=_('Clean'), default=True, null=True, blank=True)
    Clean_Operator = models.CharField(verbose_name=_('Clean_Operator'), max_length=40, null=True, blank=True)
    updatetime = models.DateTimeField(auto_now=True)
    updateuser = models.CharField(max_length=40)

    class Meta:
        db_table = 'ScreenUseHistory'


class ReceiveReturnHistory(models.Model):
    sn = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    manager = models.CharField(max_length=40)
    operator = models.CharField(max_length=40)
    operator_choices = (('receive', 'receive'), ('return', 'return'),)
    operationtype = models.CharField(max_length=10, choices=operator_choices, default='receive')
    operationtime = models.CharField(max_length=40)
    updateuser = models.CharField(max_length=40)
    updatetime = models.CharField(max_length=40)
    comment = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'ReceiveReturnHistory'


class DimensionalRecord(models.Model):
    sn = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    TestPoint = models.CharField(verbose_name=_("TestPoint"), max_length=40, null=True, blank=True)
    StandardValue = models.FloatField(verbose_name=_("StandardValue"), null=True, blank=True)
    ErrorRange = models.FloatField(verbose_name=_('ErrorRange'), null=True, blank=True)
    MeasuredValue = models.FloatField(verbose_name=_("MeasuredValue"), null=True, blank=True)

    class Meta:
        db_table = 'DimensionalRecord'
        verbose_name = _("DimensionalRecord (mm)")
        verbose_name_plural = verbose_name


class BladeWidth(models.Model):
    sn = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    Point = models.CharField(verbose_name=_("Point"), max_length=40, null=True, blank=True)
    Value = models.FloatField(verbose_name=_("Value"), null=True, blank=True)

    class Meta:
        db_table = 'BladeWidth'
        verbose_name = _("BladeWidth (mm)")
        verbose_name_plural = verbose_name


class BladeAngle(models.Model):
    sn = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    Angle = models.CharField(verbose_name=_("Angle"), max_length=40, null=True, blank=True)
    Value = models.FloatField(verbose_name=_("Value"), null=True, blank=True)

    class Meta:
        db_table = 'BladeAngle'
        verbose_name = _("BladeAngle (°)")
        verbose_name_plural = verbose_name


class C_Scrap(models.Model):
    sn = models.CharField(max_length=40, primary_key=True)
    ConsumableType = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    version = models.CharField(max_length=40)
    tooltype = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    inscrapping = models.BooleanField(default=True)
    usefullife = models.IntegerField(default=0)
    ratedlife = models.IntegerField(default=0)
    location = models.CharField(max_length=40, null=True, blank=True)
    entertime = models.CharField(max_length=100)
    updateuser = models.CharField(max_length=40)
    updatetime = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'C_Scrap'


class Spacing(models.Model):
    sn = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    Arg = models.CharField(max_length=10, verbose_name=_("Arg"), null=True, blank=True)
    StandardValue = models.FloatField(verbose_name=_("StandardValue"), null=True, blank=True)
    ErrorRange = models.FloatField(verbose_name=_('ErrorRange'), null=True, blank=True)
    Arg1 = models.CharField(max_length=10, verbose_name=_("Arg1"), null=True, blank=True)
    MeasuredValue1 = models.FloatField(verbose_name=_("MeasuredValue1"), null=True, blank=True)
    Arg2 = models.CharField(max_length=10, verbose_name=_("Arg2"), null=True, blank=True)
    MeasuredValue2 = models.FloatField(verbose_name=_("MeasuredValue2"), null=True, blank=True)

    class Meta:
        db_table = 'Spacing'
        verbose_name = _("Spacing (mm)")
        verbose_name_plural = verbose_name


class Tension(models.Model):
    sn = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    Point = models.IntegerField(verbose_name=_("Point"), null=True, blank=True)
    StandardValue = models.FloatField(verbose_name=_("StandardValue"), null=True, blank=True)
    ErrorRange = models.FloatField(verbose_name=_('ErrorRange'), null=True, blank=True)
    MeasuredValue = models.FloatField(verbose_name=_("MeasuredValue"), null=True, blank=True)

    class Meta:
        db_table = 'Tension'
        verbose_name = _("Tension (N)")
        verbose_name_plural = verbose_name
