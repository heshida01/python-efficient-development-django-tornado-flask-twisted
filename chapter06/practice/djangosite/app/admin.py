# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Moment

class MomentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("消息内容", {
            'fields': ('content', 'kind')
        }),
        ('用户信息', {
            'fields': ('user_name',),
        }),
    )

class MyAdminSite(admin.AdminSite):
    site_header = '我的管理网站'

admin_site = MyAdminSite()
admin_site.register(Moment, MomentAdmin)
#admin.site.register(Moment, MomentAdmin)
