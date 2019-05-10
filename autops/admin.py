from django.contrib import admin
from autops.models import *

# Register your models here.
@admin.register(Playbook)
class PlaybookAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'created_time', 'modified_time')
	list_filter = ('status', )
	search_fields = ('name', 'created_time', 'modified_time')


class CatalogAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'created_time', 'modified_time')
	list_filter = ('status', )
	search_fields = ('name', 'created_time', 'modified_time')


@admin.register(JobTemplate)
class JobTemplateAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'created_time', 'modified_time')
	list_filter = ('status', )
	search_fields = ('name', 'created_time', 'modified_time')