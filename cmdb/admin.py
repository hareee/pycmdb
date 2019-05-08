from django.contrib import admin

# Register your models here.
from .models import DataCenter, Rack, BusinessSystem, Host, User


@admin.register(DataCenter)
class DataCenterAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'created_time', 'modified_time')
	list_filter = ('status', )
	search_fields = ('name', 'created_time', 'modified_time')


@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'created_time', 'modified_time')
	list_filter = ('status',)
	search_fields = ('name', 'created_time', 'modified_time')


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		"""函数作用：使当前登录的用户只能看到自己负责的服务器"""
		qs = super(HostAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(user=User.objects.filter(user_name=request.user))

	list_display = ('name', 'ip', 'status', 'system', 'virtual', 'datacenter', 'rack', 'created_time', 'modified_time')
	list_filter = ('status', 'system', 'virtual', 'datacenter', 'rack', 'system__application_manager', 'system__hardware_manager',)
	search_fields = ('name', 'ip', 'created_time', 'modified_time')
	fk_fields = ('hardware_manager', 'application_manager',)

	# list_per_page设置每页显示多少条记录，默认是100条
	list_per_page = 20

	# ordering设置默认排序字段，负号表示降序排序
	ordering = ('name',)


@admin.register(BusinessSystem)
class BusinessSystemAdmin(admin.ModelAdmin):
	list_display = ('name', 'code', 'status', 'application_manager', 'hardware_manager', 'created_time', 'modified_time')
	list_filter = ('status', 'application_manager', 'hardware_manager',)
	search_fields = ('name', 'code', 'created_time', 'modified_time')

admin.site.site_header = '大数据集群运维管理平台'
admin.site.site_title = '大数据集群运维管理平台'