from django.contrib import admin

# Register your models here.
from .models import Host

class CmdbAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'owner', 'created_time', 'modified_time')
	list_filter = ('status', 'owner')
	search_fields = ('name', 'created_time', 'modified_time')

admin.site.register(Host, CmdbAdmin)