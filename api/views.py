from rest_framework import views
from rest_framework.response import Response
from fcm_django.models import FCMDevice

class Notif(views.APIView):

    def get(self, request):
        devices = FCMDevice.objects.all()

        devices.send_message(title="Title", body="Message")
        return Response({'success': True}, status="200")
