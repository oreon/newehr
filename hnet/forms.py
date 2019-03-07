from django.forms import ModelForm
from myapp.models import *

# Create the form class.
class MeasurementForm(ModelForm):
     class Meta:
        model = Measurement
        fields = ['msmtType', 'value', ]