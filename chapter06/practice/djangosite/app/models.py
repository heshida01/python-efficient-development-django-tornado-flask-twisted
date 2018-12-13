# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.  
KIND_CHOICES = (  
    ('Python技术', 'Python技术'),  
    ('数据库技术', '数据库技术'),  
    ('经济学', '经济学'),  
    ('文体资讯', '文体资讯'),  
    ('个人心情', '个人心情'),  
    ('其他', '其他'),  
)  

# Create your models here.
class Moment(models.Model):
    content = models.CharField(max_length=300, null=False)
    user_name = models.CharField(max_length = 20, default = '匿名')
    kind = models.CharField(max_length = 20, choices = KIND_CHOICES, default= KIND_CHOICES[0])
