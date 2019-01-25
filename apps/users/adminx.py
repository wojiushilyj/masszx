# -*- coding: utf-8 -*-
__author__='bobby'
__date__='2018/1/14 18:07'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Baner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "Mas后台管理"
    site_footer = "Mas在线网"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url', 'index','add_time']



xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Baner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)