from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView

# def response(status,message,data):
#     data={'status':status,'message':message,'data':data}
#     return Response(data)

response = lambda status, message, data: Response({'status': status, 'message': message, 'data': data})
