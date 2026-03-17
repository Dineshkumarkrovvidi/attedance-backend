from rest_framework import serializers
from .models import Addattedance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addattedance
        fields = '__all__'