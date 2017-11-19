#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.shortcuts import render, HttpResponse,redirect
from king_admin import king_showadmin

from forms import create_model_form
# Create your views here.


def index(request):
    # print king_showadmin.enabled_admins['crm']['customer']
    list_things = king_showadmin.enabled_admins
    # print list_things
    return render(request, 'kind_admin/index.html', {
        'list': list_things,
    })


def index_name(request, app_name, table_name):
    # print("-->", app_name, table_name)
    admin_class = king_showadmin.enabled_admins[app_name][table_name]
    # print admin_class
    return render(request, 'kind_admin/show.html', {
        'admin_class': admin_class,
    })


def table_obj_change(request, app_name, table_name, obj_id):
    admin_class = king_showadmin.enabled_admins[app_name][table_name]
    model_form_class = create_model_form(request,admin_class)
    obj=admin_class.model.objects.get(id=obj_id)
    if request.method=="POST":
        form_obj=model_form_class(request.POST,instance=obj) # instance=obj 更新
        if form_obj.is_valid():
            form_obj.save()
    else:
        form_obj=model_form_class(instance=obj)
    return render(request,'kind_admin/table_obj_change.html',{
        'app_name':app_name,
        'table_name':table_name,
        'form_obj':form_obj,

    })
