from rest_framework import serializers
from weekend.models import weekend

class weekendserializer(serializers.ModelSerializer):
    class Meta:
        model = weekend
        fields = ['id','saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        read_only_fields = ['id']