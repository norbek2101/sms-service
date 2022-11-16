from rest_framework import generics, permissions
from rest_framework.views import Response
from get_sms import Getsms
from .serializers import SendSmsSerializer

class SendSms(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SendSmsSerializer

    def post(self, request):
        serializer = SendSmsSerializer(data=request.data)
        if serializer.is_valid():
            login = "QUANTIC"
            password = "B180Ns49DnRbuPX9686R"
            nickname = "QuanticUz"

            message = Getsms(login=login, password=password, nickname=nickname)
            phone_numbers = [serializer.data['phone_number']]

            results = message.send_message(phone_numbers=phone_numbers, text=serializer.data['text'])

            if 'error' in results:
                print(results)

            for result in results:
                print(result)
            return Response({"msg": f"SMS was sent successfully to {serializer.data['phone_number']}"})
        else:
            return Response({"msg":serializer.errors})