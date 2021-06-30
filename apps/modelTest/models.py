from django.db import models

# Create your models here.
class projectOverview(models.Model):
    """项目名称
    项目类型
    项目阶段
    项目业主
    项目业主所属集团
    设计单位
    日期
    """
    projectNo = models.IntegerField(primary_key=True, verbose_name='项目序号')
    projectName = models.CharField(max_length=100, verbose_name='项目名称')
    projectType = models.CharField(max_length=20, verbose_name='项目类型')
    projectStage = models.CharField(max_length=20, verbose_name='项目阶段')
    projectHost = models.CharField(max_length=30, verbose_name='项目业主', blank=True)
    projectHostGroup = models.CharField(max_length=50, verbose_name='项目业主集团', blank=True)
    projectDesign = models.CharField(max_length=50, verbose_name='设计单位')
    projectDate = models.CharField(max_length=20, verbose_name='日期')


class siteProfile(models.Model):
    """位置
    安装容量
    用地面积
    海拔高度
    纬度
    经度
    水平太阳总辐射
    最佳辐射量倾角
    """
    projectNo = models.ForeignKey(to="projectOverview", to_field="projectNo", on_delete=models.CASCADE,
                                  primary_key=True, verbose_name='项目序号')
    location = models.CharField(max_length=50, verbose_name='项目地址')
    capacity = models.FloatField(verbose_name='安装容量')
    area = models.FloatField(verbose_name='用地面积')
    altitude = models.IntegerField(verbose_name='海拔高度')
    longtitude = models.CharField(verbose_name='经度', max_length=50)
    latitude = models.CharField(verbose_name='纬度', max_length=50)
    radiationMJ = models.FloatField(verbose_name='水平太阳总辐射MJ')
    radiationkwh = models.FloatField(verbose_name='水平太阳总辐射kwh')
    dipAngle = models.IntegerField(verbose_name='最佳辐射量倾角')


class temperature(models.Model):
    """
    多年平均气温
    多年极端最高气温
    多年极端最低气温
    最热月平均气温
    多年最大冻土深度
    多年平均风速
    多年极大风速
    多年平均雷暴日数
    污秽等级
    """
    projectNo = models.ForeignKey(to="projectOverview", to_field="projectNo", on_delete=models.CASCADE,
                                  primary_key=True, verbose_name='项目序号')
    avgTemperature = models.FloatField(verbose_name='多年平均气温')
    maxTemperature = models.FloatField(verbose_name='多年极端最高气温')
    minTemperature = models.FloatField(verbose_name='多年极端最低气温')
    avgMonthTemperature = models.FloatField(verbose_name='最热月平均气温', blank=True)
    breakingGroundDepth = models.FloatField(verbose_name='多年最大冻土深度', blank=True)
    avgSpeed = models.FloatField(verbose_name='多年平均风速', blank=True)
    maxSpeed = models.FloatField(verbose_name='多年最大风速', blank=True)
    rainyDays = models.FloatField(verbose_name='多年平均雷暴日数', blank=True)
    pollutionLevel = models.FloatField(blank=True, verbose_name='污秽等级')
