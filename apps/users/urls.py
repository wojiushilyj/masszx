# -*- coding: utf-8 -*-
__author__ = 'oPcoApexo'
__date__ = '2019/6/20 0020 17:30'

from django.urls import path, include,re_path
from .views import UserinfoView,UploadImageView,UpdatePwdView,SendEmailCodeView,UpdateEmailView
from .views import MyCourseView,MyFavOrgView,MyFavTeacherView,MyFavCourseView,MymessageView
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

    #我的课程
    re_path(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),

    #我收藏的课程机构
    re_path(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),

    #我收藏的授课讲师
    re_path(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),

    #我收藏的课程
    re_path(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),

    # 我的消息
    re_path(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),

]