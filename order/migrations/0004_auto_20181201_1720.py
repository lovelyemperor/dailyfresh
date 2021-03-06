# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-01 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20181118_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='trance_num',
            field=models.CharField(default='', max_length=100, verbose_name='支付编号'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='comment',
            field=models.CharField(default='', max_length=128, verbose_name='评论'),
        ),
    ]
