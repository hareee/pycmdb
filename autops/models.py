from django.db import models
from django.forms import Textarea

# Create your models here.
class Playbook(models.Model):
	STATUS_NORMAL = 1
	STATUS_DELETE = 0
	STATUS_ITEMS = (
		(STATUS_NORMAL, '正常'),
		(STATUS_DELETE, '删除'),
	)

	name = models.CharField(max_length=50, verbose_name="名称")
	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
	comment = models.CharField(max_length=50, verbose_name="备注")
	content = models.CharField(max_length=50, verbose_name="内容")
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	modified_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")

	class Meta:
		verbose_name = verbose_name_plural = '剧本'

	def __str__(self):
		return self.name


class Catalog(models.Model):
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
		verbose_name = verbose_name_plural = '作业分类'

	def __str__(self):
		return self.name

class Inventory(models.Model):
	STATUS_NORMAL = 1
	STATUS_DELETE = 0
	STATUS_ITEMS = (
		(STATUS_NORMAL, '正常'),
		(STATUS_DELETE, '删除'),
	)

	name = models.CharField(max_length=50, verbose_name="名称")
	organization = models.CharField(max_length=50, verbose_name="组织机构")
	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	modified_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")

	class Meta:
		verbose_name = verbose_name_plural = 'Inventory'

	def __str__(self):
		return self.name

class JobTemplate(models.Model):
	STATUS_NORMAL = 1
	STATUS_DELETE = 0
	STATUS_ITEMS = (
		(STATUS_NORMAL, '正常'),
		(STATUS_DELETE, '删除'),
	)

	TYPE_RUN = 1
	TYPE_CHECK = 0
	TYPE_PROMPT = 2
	TYPE_ITEMS = (
		(TYPE_RUN, '运行'),
		(TYPE_CHECK, '检查'),
		(TYPE_PROMPT, '提示'),
	)


	name = models.CharField(max_length=50, verbose_name="名称")
	desc = models.CharField(max_length=50, verbose_name="描述")
	type = models.PositiveIntegerField(default=TYPE_CHECK, choices=TYPE_ITEMS, verbose_name="类型")
	#Inventory: Choose the inventory to be used with this job template from the inventories available to the currently
	# logged in Tower user.

	#Playbook:Choose the playbook to be launched with this job template from the available playbooks.
	# This menu is automatically populated with the names of the playbooks found in the project base path for the selected project.
	# For example, a playbook named “jboss.yml” in the project path appears in the menu as “jboss”.

	#Credential

	#Forks:The number of parallel or simultaneous processes to use while executing the playbook
	# A value of zero uses the Ansible default setting, which is 5 parallel processes unless overridden
	# in /etc/ansible/ansible.cfg

	#Limit:A host pattern to further constrain the list of hosts managed or affected by the playbook
	# Multiple patterns can be separated by colons (”:”).
	# As with core Ansible, “a:b” means “in group a or b”, “a:b:&c” means “in a or b but must be in c”,
	# and “a:!b” means “in a, and definitely not in b”.

	#Verbosity: Control the level of output Ansible produces as the playbook executes

	#Job Tags:If you have a large playbook, it may become useful to be able to run only a specific part of it
	# rather than running everything in the playbook. Ansible supports a “tags:” attribute for this reason.

	#@Labels:Supply optional labels that describe this job template, such as “dev” or “test”.
	# Labels can be used to group and filter job templates and completed jobs in the Tower display.

	#extra_var:

	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	modified_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")

	class Meta:
		verbose_name = verbose_name_plural = '作业模板'

	def __str__(self):
		return self.name


