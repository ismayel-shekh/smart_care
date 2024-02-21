from django.db import models
from patient.models import patient
from doctor.models import Doctor, AvailableTime
# Create your models here.
APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('pending', 'pending'),
    ('Running', 'Running'),
]
APPOINTMENT_TYPES =[
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]
class Appointment(models.Model):
    patient = models.ForeignKey(patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    appointment_types = models.CharField(choices = APPOINTMENT_TYPES, max_length =10)
    appointment_status = models.CharField(choices = APPOINTMENT_STATUS, max_length =10, default = "Pending")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} , {self.patient.user.first_name}"