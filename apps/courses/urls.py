# -*- coding: utf-8 -*-
__author__ = 'bobby'
__date__ = '2019/2/26 0026 8:41'

from django.urls import path, include,re_path

from .views import CourseListView,CourseDetailView,CourseInfoView,CommentsView,AddComentsView
app_name = "organization"


urlpatterns = [
    # 课程列表页
    re_path(r'^list/$', CourseListView.as_view(), name="course_list"),
    #课程详情页
    re_path(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    #课程信息页
    re_path(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    #课程评论
    re_path(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),

    #添加课程评论
    re_path(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),
]