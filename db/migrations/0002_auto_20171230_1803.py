# Generated by Django 2.0 on 2017-12-30 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='db_mysql',
            options={'permissions': {('read_db_mysql', '只读数据库资产'), ('task_db_mysql', '执行数据库资产')}, 'verbose_name': '数据库管理', 'verbose_name_plural': '数据库管理'},
        ),
    ]
