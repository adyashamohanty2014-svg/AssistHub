from rest_framework import serializers
from .models import Device
#ModelSerializer saves time by generating the fields from your model
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'