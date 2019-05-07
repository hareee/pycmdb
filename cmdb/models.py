# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Host(models.Model):
	STATUS_NORMAL = 1
	STATUS_DELETE = 0
	STATUS_ITEMS = (
		(STATUS_NORMAL, '正常'),
		(STATUS_DELETE, '删除'),
	)

	name = models.CharField(max_length=50, verbose_name="名称")
	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
	owner = models.ForeignKey(User, verbose_name="属主", on_delete=models.DO_NOTHING)
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	modified_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")


	class Meta:
		verbose_name = verbose_name_plural = '主机'


	def __str__(self):
		return self.name