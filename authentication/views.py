from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import PacientSerializer
from .models import Pacient
from django.contrib.auth.models import User

class PacientViewSet(viewsets.ViewSet):
    queryset = Pacient.objects.all()

    def create(self, request):
        message = "error"  
        email = request.data.get('email', False)
        password = request.data.get('password', False)
        name = request.data.get('name', False)
        phone = request.data.get('phone', False)

        if email and password and name and phone:
            user = User.objects.create_user(email, email, password)
            Pacient.objects.create(name=name, phone=phone, user=user)
            message = "Pacient created Sucefully"
        
        return Response(message, status = status.HTTP_201_CREATED)

