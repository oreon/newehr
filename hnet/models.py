from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.

class MeasurementType(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

FREQ_CHOICES = (
    (1, "Daily"),
    (7, "Weekly"),
    (30, "Monthly"),
    (90, "Quarterly"))


class GroupMeasurementTemplate(models.Model):
    frequency = models.IntegerField(choices=FREQ_CHOICES, default=1) 
    patient = models.ForeignKey(User, related_name="pt_grpmsmt", on_delete = models.CASCADE)
    msmtType = models.ManyToManyField(MeasurementType)

    def __str__(self):
        return self.patient.__str__() + " "  + str(self.frequency)

class GroupMeasurement(models.Model):
    groupMeasurement = models.ForeignKey('GroupMeasurementTemplate', 
        related_name='groupMeasurementTemplate',  on_delete=models.CASCADE)
    date =  models.DateTimeField(default = timezone.now)
    comments = models.TextField(blank = True, null = True)        

class GroupMeasurementRecording(models.Model):
    msmtType = models.ForeignKey(MeasurementType, related_name="groupMeasurementRecording", on_delete = models.CASCADE)
    groupMeasurement = models.ForeignKey('GroupMeasurement', related_name='groupMeasurementRecording',  on_delete=models.CASCADE)
    value = models.DecimalField(max_digits = 5, decimal_places = 2,)

class Measurement(models.Model):
    patient = models.ForeignKey(User, related_name="pt_msmt", on_delete = models.CASCADE)
    msmtType = models.ForeignKey(MeasurementType, related_name="msmtType", on_delete = models.CASCADE)
    value = models.DecimalField(max_digits = 5, decimal_places = 2,)
    created =  models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.msmtType.__str__() + " "  + str(self.value)


