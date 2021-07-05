from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Pacient
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action

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

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated], authentication_classes=[TokenAuthentication])
    def pacient_personal_info(self, request, format=None):
        pacient = Pacient.objects.get(user = request.user)
        content = {
            'id': pacient.id,
            'name': pacient.name,  
            'phone': pacient.phone,  
        }
        return Response(content, status = status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def login(request, format=None):
    content = {
        'user': str(request.user),  
        'auth': str(request.auth),  
    }
    return Response(content)