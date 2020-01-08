from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    company_name = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    zip = serializers.IntegerField(required=False)
    email = serializers.EmailField(required=False)
    web = serializers.URLField(required=False)

    class Meta:
        model = User
        fields = '__all__'