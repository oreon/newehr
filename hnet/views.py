from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Measurement
from django.urls import reverse
from django.contrib import messages


import django_tables2 as tables


class MsmtTable(tables.Table):
    class Meta:
        model = Measurement
        template_name = 'django_tables2/bootstrap.html'
# Create your views here.
class MeasurementList(ListView): 
    model = Measurement

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['table'] =  MsmtTable(Measurement.objects.filter(patient = self.request.user))
        return context

    def get_queryset(self):
        return  Measurement.objects.filter(patient = self.request.user)


class MeasurementDetail(DetailView): 
    model = Measurement
class MeasurementCreate(CreateView): 
    model = Measurement
    fields = ['msmtType', 'value', 'comments']
    success_url = '/msmt/measurements'  #reverse('hnet:mesurement_list')

    def form_valid(self, form):
        form.instance.patient = self.request.user
        messages.success(self.request, 'Successfully created')
        return super().form_valid(form)




class MeasurementUpdate(UpdateView): 
    model = Measurement
    fields = ['msmtType', 'value', ]
    success_url = '/msmt/measurements'  #reverse('hnet:mesurement_list')

class MeasurementDelete(DeleteView): 
    model = Measurement