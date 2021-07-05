from django.db import models
from authentication.models import Pacient

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        
class Schedule(models.Model):
    initial_time = models.DateTimeField()
    final_time = models.DateTimeField()
    def __str__(self):
        return str(self.initial_time) + ' - ' + str(self.final_time)
    is_scheduled = models.BooleanField(default=None)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Appointment(models.Model):
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    pacient = models.OneToOneField(Pacient, on_delete=models.CASCADE)
    def __str__(self):
        return 'Medico: ' + str(self.schedule.doctor.name) + ' Paciente: ' + str(self.pacient.name)
