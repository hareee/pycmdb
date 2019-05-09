from django.shortcuts import render

# Create your views here.
from cmdb.models import Host
from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from cmdb.serializers import HostSerializer

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

def discover(request):
    data = JSONParser().parse(request)
    serializer = HostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Create your views here.
class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer