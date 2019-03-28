from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import serializers


from rest_framework_simplejwt.tokens import RefreshToken
import json
from fcm_django.models import FCMDevice


class Login(views.APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")

        username = request.data['username']
        password = request.data['password']

        try:
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        if user:
            refresh = RefreshToken.for_user(user)
            token = json.dumps({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            print(token)
            data = serializers.serialize('json', [user])
            data = data[1:len(data)-2]
            data = data+', "token": '+token+'}'
            print(data)
            return Response(
              data,
              status=200,
              content_type="application/json"
            )
        else:
            return Response(
              json.dumps({'Error': "Invalid credentials"}),
              status=400,
              content_type="application/json"
            )

class Notif(views.APIView):

    def get(self, request):
        devices = FCMDevice.objects.all()

        devices.send_message(title="Title", body="Message")
        return Response({'success': True}, status="200")
