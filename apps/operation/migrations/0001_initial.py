# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-22 12:49
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20170522_1249'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderCode', models.CharField(max_length=100, verbose_name='\u8ba2\u5355\u53f7')),
                ('address', models.CharField(max_length=100, verbose_name='\u6536\u8d27\u5730\u5740')),
                ('post', models.CharField(max_length=100, verbose_name='\u90ae\u653f\u7f16\u7801')),
                ('receiver', models.CharField(max_length=100, verbose_name='\u6536\u8d27\u4eba\u4fe1\u606f')),
                ('mobile', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('userMessage', models.CharField(max_length=100, verbose_name='\u7528\u6237\u5907\u6ce8\u4fe1\u606f')),
                ('createDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('payDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u652f\u4ed8\u65e5\u671f')),
                ('deliveryDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u8d27\u65e5\u671f')),
                ('confirmDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u786e\u8ba4\u6536\u8d27\u65e5\u671f')),
                ('status', models.CharField(choices=[('waitPay', '\u7b49\u5f85\u652f\u4ed8'), ('waitDelivery', '\u7b49\u5f85\u53d1\u8d27'), ('waitConfirm', '\u7b49\u5f85\u6536\u8d27'), ('finish', '\u4ea4\u6613\u5b8c\u6210'), ('delete', '\u8ba2\u5355\u5220\u9664')], default='waitPay', max_length=100, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='\u8d2d\u4e70\u6570\u91cf')),
                ('status', models.CharField(choices=[('default', '\u521d\u59cb\u72b6\u6001'), ('waitReview', '\u7b49\u5f85\u8bc4\u4ef7'), ('finish', '\u4ea4\u6613\u5b8c\u6210')], default='default', max_length=20, verbose_name='\u8ba2\u5355\u9879\u72b6\u6001')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.Order', verbose_name='\u8ba2\u5355')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='\u4ea7\u54c1')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u9879',
                'verbose_name_plural': '\u8ba2\u5355\u9879',
            },
        ),
    ]
