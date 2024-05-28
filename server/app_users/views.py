from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import permission_required

from .models import User
from .serializer import UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import exceptions

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data, "message": 'Lista generada correctamente', "status":200})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['POST'])
@permission_classes([AllowAny])
def add_user(request):
    if request.method == 'POST':
        data = request.data if request.content_type == 'application/json' else request.POST.dict()
        serializer = UserSerializer(data=data)
        if User.objects.filter(email=data['email']).exists():
            return Response({"message": 'El correo ya existe', "status":400})
        if serializer.is_valid():
            serializer.save()
            return Response({"user": serializer.data, "message": 'Usuario creado correctamente', "status":201})
        return Response({"message": 'Error al crear usuario', "status":400})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@permission_required('app_users.view_user', raise_exception=True)
def get_user(request, pk):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response({"user": serializer.data, "message": 'Usuario encontrado', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Usuario no encontrado', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, pk):
    if request.method == 'PUT':
        try:
            user = User.objects.get(pk=pk)
            data = request.data if request.content_type == 'application/json' else request.POST.dict()
            data.pop('id', None)
            data.pop('password', None)
            serializer = UserSerializer(user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"user": serializer.data, "message": 'Usuario actualizado', "status":200})
            return Response({"message": 'Error al actualizar usuario', "status":400})
        except ObjectDoesNotExist:
            return Response({"message": 'Usuario no encontrado', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_password(request, pk):
    if request.method == 'PUT':
        try:
            user = User.objects.get(pk=pk)
            data = request.data if request.content_type == 'application/json' else request.POST.dict()
            UserSerializer().update_password(user, data)
            return Response({"message": 'Contraseña actualizada', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Usuario no encontrado', "status":404})
        except exceptions.AuthenticationFailed as e:
            return Response({"message": str(e), "status":400})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(pk=pk)
            user.is_active = False
            user.save() 
            #user.delete() No podemos eliminar, solamente desactivar
            return Response({"message": 'Usuario eliminado', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Usuario no encontrado', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})
