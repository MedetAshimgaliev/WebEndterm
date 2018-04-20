from rest_framework import serializers
from .models import postapi

class blogSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model=postapi
        fields = '__all__'
