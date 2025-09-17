from rest_framework import serializers

class VendorSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=255)
    email=serializers.EmailField(max_length=255)
    phone=serializers.CharField(max_length=20)
    company_name=serializers.CharField(max_length=255)