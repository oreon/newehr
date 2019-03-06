from django.urls import path, include

from healthnet import views
from healthnet import views_admin
from healthnet import views_admission
from healthnet import views_appointment
from healthnet import views_medtest
from healthnet import views_message
from healthnet import views_prescription
from healthnet import views_profile
from healthnet import views_medicalInfo


urlpatterns = [
                       path('', views.login_view, name='index'),
                       path('logout/', views.logout_view, name='logout'),
                       path('register/', views.register_view, name='register'),

                       #path('message/list/', views_message.message_view, name='message/list'),
                       #path('message/read/', views_message.read_view, name='message/read'),
                       #path('message/new/', views_message.new_view, name='message/new'),

                       path('admin/users/', views_admin.users_view, name='admin/users'),
                       path('admin/activity/', views_admin.activity_view, name='admin/activity'),
                       path('admin/stats/', views_admin.statistic_view, name='admin/stats'),
                       path('admin/createemployee/', views_admin.createemployee_view, name='admin/createemployee'),

                       path('message/list/', views_message.list_view, name='message/list'),
                       path('message/new/', views_message.new_view, name='message/new'),
                       path('message/read/', views_message.read_view, name='message/read'),

                       path('appointment/list/', views_appointment.list_view, name='appointment/list'),
                       path('appointment/update/', views_appointment.update_view, name='appointment/update'),
                       path('appointment/create/', views_appointment.create_view, name='appointment/create'),
                       path('appointment/cancel/', views_appointment.cancel_view, name='appointment/cancel'),

                       path('profile/', views_profile.profile_view, name='profile'),
                       path('profile/update/', views_profile.update_view, name='profile/update'),
                       path('profile/password/', views_profile.password_view, name='profile/password'),

                       path('medtest/upload/', views_medtest.create_view, name='medtest/upload'),
                       path('medtest/list/', views_medtest.list_view, name='medtest/list'),
                       path('medtest/display/', views_medtest.display_view, name='medtest/display'),
                       path('medtest/update/', views_medtest.update_view, name='medtest/update'),

                       path('admission/admit/', views_admission.admit_view, name='admission/admit'),
                       path('admission/list/', views_admission.list_view, name='admission/list'),
                       path('admission/discharge/', views_admission.discharge_view, name='admission/discharge'),

                       path('error/denied/', views.error_denied_view, name='error/denied'),

                       path('prescription/create/', views_prescription.create_view, name='prescription/create'),
                       path('prescription/list/', views_prescription.list_view, name='prescription/list'),
                       path('prescription/delete/', views_prescription.delete_view, name='prescription/delete'),

                       path('medicalinfo/list/', views_medicalInfo.list_view, name='medicalinfo/list'),
                       path('medicalinfo/update/', views_medicalInfo.update_view, name='medicalinfo/update'),
                       path('medicalinfo/patient/', views_medicalInfo.patient_view, name='medicalinfo/patient'),
]