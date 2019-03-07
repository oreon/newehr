from django.contrib import admin



from .models import *

admin.site.register(Measurement)
admin.site.register( MeasurementType)
#admin.site.register(GroupMeasurement)
admin.site.register(GroupMeasurementTemplate)


#@admin.register(CustomerOrder)
class GroupMeasurementRecordingInline (admin.TabularInline):
    model = GroupMeasurementRecording

@admin.register(GroupMeasurement)
class GroupMeasurementAdmin (admin.ModelAdmin):
    inlines = [ GroupMeasurementRecordingInline]

# Register your models here.
