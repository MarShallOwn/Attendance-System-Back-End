from rest_framework import serializers
from holiday.models import holiday

class holidayserializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['startDate'] > attrs['endDate']:
            raise serializers.ValidationError({'startDate' :'must be bigger than endDate'})
        return attrs
    class Meta:
        model = holiday
        fields = ['id','name','type','startDate','noOfDays','endDate']
        read_only_fields = ['id']