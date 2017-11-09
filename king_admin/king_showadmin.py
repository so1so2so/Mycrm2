#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from crm import models

enabled_admins = {}


class BaseAdmin(object):
    list_display = []


class CustomerAdmin(BaseAdmin):
    list_display = ['name', 'qq', 'qq_name', ]
    # model = models_class

class MenuAdmin(BaseAdmin):
    list_display = ['name', 'url_name',  ]

# 这个函数传递2个值进去 一个是models的表名,一个是自定义的类名
def regist(model_class, admin_class=None):
    # _meta.app_label 是找出app名称 _meta.model_name是找出表名称
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label] = {}
        # 原来的是 admin.site.register(models.Customer, CustomerAdmin)
        # 相当于把CustomerAdmin这个类新加一个model的属性,把这2个属性传递进去
    admin_class.model = model_class  # 绑定model 对象和admin 类
    # 定义数组里面嵌套的数组,类型相当于{app_name:{table_name:admin_class}} admin_class可以找出对应的列
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class
    # enabled_admins['crm']['Customer'] = CustomerAdmin
regist(models.Customer,CustomerAdmin)
regist(models.Menu,MenuAdmin)