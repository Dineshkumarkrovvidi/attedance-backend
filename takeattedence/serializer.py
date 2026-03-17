from rest_framework import serializers
from .models import Takeattedence

class Attendance1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Takeattedence
        fields = '__all__'