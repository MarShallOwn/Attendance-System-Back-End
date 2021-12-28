from rest_framework import serializers
from attendence.models import attendence

class attendenceserializer(serializers.ModelSerializer):
    class Meta:
        model = attendence
        fields = '__all__'
        read_only_fields = ['id']
   