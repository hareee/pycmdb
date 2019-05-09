# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    realname = models.TextField(default='', blank=True)

# Create your models here.
class DataCenter(models.Model):
	STATUS_NORMAL = 1
	STATUS_DELETE = 0
	STATUS_ITEMS = (
		(STATUS_NORMAL, '正常'),
		(STATUS_DELETE, '删除'),
	)

	name = models.CharField(max_length=50, verbose_name="名称")
	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	modified_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")

	class Meta:
		verbose_name = verbose_name_plural = '机房'

	def __str__(self):
		return self.name


# Create your models here.
class BusinessSystem(models.Model):
	STATUS_NORMAL = 1
	STATUS_DELETE = 0
	STATUS_ITEMS = (
		(STATUS_NORMAL, '正常'),
		(STATUS_DELETE, '删除'),
	)

	name = models.CharField(max_length=50, verbose_name="名称")
	code = models.CharField(max_length=50, verbose_name="编码", null=True)
	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
	hardware_manager = models.ForeignKey(User, related_name='hardware_manager', verbose_name="平台管理员",
	                                     on_delete=models.DO_NOTHING, null=True)
	application_manager = models.ForeignKey(User, related_name='application_manager', verbose_name="应用管理员",
	                                        on_delete=models.DO_NOTHING, null=True)
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	modified_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")


	class Meta:
		verbose_name = verbose_name_plural = '系统'


	def __str__(self):
		return self.name


# Create your models here.
class Rack(models.Model):
	STATUS_NORMAL = 1
	STATUS_DELETE = 0
	STATUS_ITEMS = (
		(STATUS_NORMAL, '正常'),
		(STATUS_DELETE, '删除'),
	)

	name = models.CharField(max_length=50, verbose_name="名称")
	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	modified_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")

	class Meta:
		verbose_name = verbose_name_plural = '机柜'

	def __str__(self):
		return self.name


# Create your models here.
class Host(models.Model):
	STATUS_NORMAL = 1
	STATUS_DELETE = 0
	STATUS_ITEMS = (
		(STATUS_NORMAL, '正常'),
		(STATUS_DELETE, '删除'),
	)

	SOURCE_MANUAL = 1
	SOURCE_SCAN = 0
	SOURCE_ITEMS = (
		(SOURCE_MANUAL, '人工录入'),
		(SOURCE_SCAN, '自动扫描'),
	)

	VERIFY_WAIT = 0
	VERIFY_PASS = 1
	VERIFY_FAIL = 2
	VERIFY_NOT = 3
	VERIFY_ITEMS = (
		(VERIFY_WAIT, '待审核'),
		(VERIFY_PASS, '审核通过'),
		(VERIFY_FAIL, '审核不通过'),
		(VERIFY_NOT, '不审核'),
	)

	VIRTUAL_YES = 1
	VIRTUAL_NO = 0
	VIRTUAL_ITEMS = (
		(VIRTUAL_YES, '虚拟机'),
		(VIRTUAL_NO, '物理机'),
	)

	name = models.CharField(max_length=50, verbose_name="名称", unique=True)
	ip = models.CharField(max_length=50, verbose_name="IP", null=True, blank=True, unique=True)
	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="使用状态")
	verify = models.PositiveIntegerField(default=VERIFY_PASS, choices=VERIFY_ITEMS, verbose_name="审核情况")
	source = models.PositiveIntegerField(default=SOURCE_MANUAL, choices=SOURCE_ITEMS, verbose_name="来源")
	datacenter = models.ForeignKey(DataCenter, on_delete=models.DO_NOTHING, verbose_name=u'机房', null=True, blank=True)
	rack = models.ForeignKey(Rack, on_delete=models.DO_NOTHING, verbose_name=u'机柜', null=True, blank=True)
	system = models.ForeignKey(BusinessSystem, on_delete=models.CASCADE, verbose_name=u'业务系统', null=True)
	virtual = models.PositiveIntegerField(default=VIRTUAL_NO, choices=VIRTUAL_ITEMS, verbose_name="虚拟化", null=True, blank=True)
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	modified_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")


	class Meta:
		verbose_name = verbose_name_plural = '主机'


	def __str__(self):
		return self.name
