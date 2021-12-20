from rest_framework import serializers
from role.models import role

class roleserializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = ['id','roleName','roleDesc']
        read_only_fields = ['id']
   