from rest_framework import serializers
from cmdb.models import Host


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        #instance.name = validated_data.get('name', instance.name)
        #instance.IP = validated_data.get('IP', instance.IP)
        #instance.status = Host.STATUS_NORMAL
        #instance.verify = Host.VERIFY_WAIT
        #instance.source = Host.SOURCE_SCAN
        #instance.virtual = validated_data.get('virtual', instance.virtual)
        #instance.save()
        #return instance
        return Host.objects.create(**validated_data)

