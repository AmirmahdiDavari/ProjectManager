from rest_framework.response import Response
from django.shortcuts import render, redirect

response = lambda status, message, data: Response({'status': status, 'message': message, 'data': data})


def adminpage(request):
    return render(request, 'adminpage.html')
