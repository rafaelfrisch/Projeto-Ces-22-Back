from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from .models import Doctor, Schedule, Appointment
from .serializers import ScheduleSerializer

class ScheduleViewSet(viewsets.ViewSet):
    queryset = Schedule.objects.all()

    def list(self, request):
        free_schedules = Schedule.objects.filter(is_scheduled=False)
        serializer = ScheduleSerializer(free_schedules, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

