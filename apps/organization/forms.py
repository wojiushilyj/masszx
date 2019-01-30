# -*- coding: utf-8 -*-
__author__ = 'bobby'
__date__ = '2019/1/29 0029 16:34'
from django import forms

from operation.models import UserAsk



class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

