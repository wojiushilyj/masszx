# -*- coding: utf-8 -*-
__author__ = 'bobby'
__date__ = '2019/1/29 0029 16:48'

from django.urls import path, include,re_path
from .views import OrgView,AdduserAskView, OrgHomeView

app_name = "organization"

urlpatterns = [
    # 课程机构列表页
    re_path(r'^list/$', OrgView.as_view(), name="org_list"),
    re_path(r'^add_ask/$', AdduserAskView.as_view(), name="add_ask"),
    re_path(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
]