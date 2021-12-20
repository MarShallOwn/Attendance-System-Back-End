from rest_framework import serializers
from department.models import department

class departmentserializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ['id','departmentName','departmentDesc','departmentHeadID']
        read_only_fields = ['id']
   