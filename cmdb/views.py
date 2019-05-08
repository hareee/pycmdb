from django.shortcuts import render

# Create your views here.
from cmdb.models import Host
from cmdb.serializers import HostSerializer
import json
from django.http import JsonResponse

from rest_framework import viewsets

def __get_response_json_dict(data, err_code=0, message="Success"):
    ret = {
        'err_code': err_code,
        'message': message,
        'data': data
    }
    return ret

def inventory(request):
    inventory = {}
    hosts = Host.objects.all().exclude(ip__isnull=True).exclude(ip__exact='')
    for host in hosts:
        group = host.system.code
        if not group in inventory:
            inventory[group] = {
                'hosts': []
            }
        inventory[group]['hosts'].append(host.ip)
    response_data = inventory

    return JsonResponse(
        __get_response_json_dict(data=response_data)
    )

# Create your views here.
class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer