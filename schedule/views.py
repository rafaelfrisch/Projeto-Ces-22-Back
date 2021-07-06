from django.db.models import query
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Doctor, Schedule, Appointment
from .serializers import ScheduleSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

class ScheduleViewSet(viewsets.ViewSet):
    queryset = Schedule.objects.all()

    def list(self, request):
        free_schedules = Schedule.objects.filter(is_scheduled=False)
        serializer = ScheduleSerializer(free_schedules, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated], authentication_classes=[TokenAuthentication])
    def make_appointment(self, request, format=None):
        message = "error"
        user = request.user
        pacient = user.pacient
        schedule_id = request.data.get('schedule_id', False)
        if schedule_id:
            schedule = get_object_or_404(Schedule, id=schedule_id)
            schedule.is_scheduled = True
            schedule.save()
            Appointment.objects.create(schedule=schedule, pacient=pacient)
            message = "Appointment created Sucefully"

        return Response(message, status = status.HTTP_201_CREATED)