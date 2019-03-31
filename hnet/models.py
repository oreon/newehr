from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class MeasurementType(models.Model):
    name = models.CharField(max_length = 20)
    min = models.IntegerField(default = 0)
    max = models.IntegerField(default = 10)
    
    def __str__(self):
        return self.name

FREQ_CHOICES = (
    (1, "Daily"),
    (7, "Weekly"),
    (30, "Monthly"),
    (90, "Quarterly"),
    (182, "Semi annually"),
    (365, "Annually"),
    )


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
    patient = models.ForeignKey('healthnet.Patient', related_name="measurements", on_delete = models.CASCADE)
    measurementType = models.ForeignKey(MeasurementType, related_name="msmtType", on_delete = models.CASCADE)
    value = models.DecimalField(max_digits = 5, decimal_places = 2,)
    created =  models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank = True, null = True)

    # def clean(self): 
    #     print (self.value)
    #     errors = {}
    #     #dia i hora sempre informats     
    #     if self.value < self.msmtType.min or self.value > self.msmtType.max:   #<-- business rules
    #         errors.setdefault('range error',[])\
    #         .append(u'Value must be between {} and {}'.format( self.msmtType.min , self.msmtType.max))
    #     if len( errors ) > 0: 
    #         raise ValidationError(errors)  #<-- raising errors

    # def save(self, *args, **kwargs):
    #     print(**kwargs)
    #     self.full_clean()
    #     return super(MeasurementType, self).save(*args, **kwargs)

    def __str__(self):
        return self.msmtType.__str__() + " "  + str(self.value)


