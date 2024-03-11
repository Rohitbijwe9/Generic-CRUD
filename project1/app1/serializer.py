from rest_framework import serializers
from .models import Studet




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Studet
        fields='__all__'
        