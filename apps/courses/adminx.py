# -*- coding: utf-8 -*-
__author__ = 'bobby'
__date__ = '2019/1/14 0014 18:56'
import xadmin
from .models import Course,Lesson,Video,CourseResource

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree','learn_times', 'students', 'fav_nums', 'image','click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree','learn_times', 'students', 'fav_nums', 'image','click_nums', 'add_time']

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
