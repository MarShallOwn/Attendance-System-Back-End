from rest_framework import serializers
from .models import LeaveRequest
class LeaveRequestSerializer(serializers.ModelSerializer): 
    startDate = serializers.DateField(input_formats=['%m-%d-%Y'])
    endDate = serializers.DateField(input_formats=['%m-%d-%Y'])
    def validate(self, attrs):
        if attrs['startDate'] >= attrs['endDate']:
            raise serializers.ValidationError({'startDate' :'must be less than endDate'})
        return attrs
    class Meta:
        model  = LeaveRequest  
        fields = ['id','typeOfLeave','description','startDate','endDate','user']
        read_only_fields = ['id']

class LeaveRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields=['status']