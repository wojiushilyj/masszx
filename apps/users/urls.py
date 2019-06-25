# -*- coding: utf-8 -*-
__author__ = 'oPcoApexo'
__date__ = '2019/6/20 0020 17:30'

from django.urls import path, include,re_path
from .views import UserinfoView,UploadImageView,UpdatePwdView,SendEmailCodeView,UpdateEmailView
app_name = "users"

urlpatterns = [
    # 用户信息
    re_path(r'^info/$', UserinfoView.as_view(), name="user_info"),

    #用户头像上传
    re_path(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    #用户个人中心修改密码
    re_path(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    #发送邮箱验证码
    re_path(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    #修改邮箱
    re_path(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

]