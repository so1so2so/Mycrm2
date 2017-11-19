#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.forms import forms, ModelForm

from crm import models


class CustoModelForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'


# 动态生成类
def create_model_form(request, admin_class):
    '''动态生成ModeForm'''

    class Meta:
        model = admin_class.model
        fields = '__all__'
    attrs= {'Meta': Meta}
    _model_form_class = type("DynamicModelForm", (ModelForm,),attrs)
    print _model_form_class.Meta.model
    return _model_form_class
