from rest_framework import serializers
from weekend.models import weekend

class weekendserializer(serializers.ModelSerializer):
    class Meta:
        model = weekend
        fields = '__all__'
        read_only_fields = ['id']