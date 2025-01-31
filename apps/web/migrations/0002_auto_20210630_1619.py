# Generated by Django 3.2 on 2021-06-30 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PVSystem',
            fields=[
                ('projectNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.projectoverview', verbose_name='项目序号')),
                ('component', models.IntegerField(blank=True, verbose_name='组件')),
                ('installedAngle', models.IntegerField(blank=True, verbose_name='固定安装倾角')),
                ('plan', models.IntegerField(blank=True, verbose_name='组串方案')),
                ('inverter', models.IntegerField(blank=True, verbose_name='逆变器')),
                ('capacityRatio', models.FloatField(blank=True, verbose_name='组件与逆变器容配比')),
                ('inclinedRadiation', models.FloatField(blank=True, verbose_name='倾斜面辐射量')),
                ('systemEffience', models.FloatField(blank=True, verbose_name='系统效率')),
                ('avgElectricity', models.FloatField(blank=True, verbose_name='25年均上网电量')),
                ('avgHours', models.FloatField(blank=True, verbose_name='25年均小时数')),
                ('firstYearHours', models.FloatField(blank=True, verbose_name='首年利用小时数')),
                ('firstConnect', models.CharField(blank=True, max_length=20, verbose_name='首次并网')),
                ('fullConnect', models.CharField(blank=True, max_length=20, verbose_name='全容量并网')),
            ],
            options={
                'verbose_name': '光伏发电系统及发电量',
                'verbose_name_plural': '光伏发电系统及发电量',
            },
        ),
        migrations.AlterModelOptions(
            name='projectoverview',
            options={'verbose_name': '项目概况', 'verbose_name_plural': '项目概况'},
        ),
        migrations.AlterModelOptions(
            name='siteprofile',
            options={'verbose_name': '场址概况', 'verbose_name_plural': '场址概况'},
        ),
        migrations.AlterModelOptions(
            name='temperature',
            options={'verbose_name': '主要气象特征要素', 'verbose_name_plural': '主要气象特征要素'},
        ),
    ]
