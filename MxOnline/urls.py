"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from users.views import LoginView, RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    # 基于函数 的 View 映射 URL 方法
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    # 验证码
    path('captcha/', include('captcha.urls')),
    # 验证用户注册后，在邮件里点击注册链接
    re_path(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    # 忘记密码
    re_path(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # 用户在邮件里点击重置密码链接
    re_path(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    # 重置密码表单 POST 请求
    re_path(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    #课程机构首页
    re_path(r'^org_list/$', OrgView.as_view(), name="org_list"),
    #配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)$',serve ,{"document_root":MEDIA_ROOT}),


]