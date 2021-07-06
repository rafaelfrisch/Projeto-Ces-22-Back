from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.name')

    class Meta:
        model = Schedule
        fields = ['initial_time', 'final_time', 'doctor', 'doctor_name']