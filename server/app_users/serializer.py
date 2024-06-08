#Serializar para el modelo de usuario
from rest_framework import serializers
from .models import User

from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'email', 'password', 'first_name', 'last_name', 'phone', 'is_active', 'is_superuser', 'is_staff' ,'last_login'
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
    
    def update_password(self, instance, validated_data):
        if not instance.check_password(validated_data['password']):
            raise exceptions.AuthenticationFailed('Contraseña incorrecta')
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD
    
    def validate(self, attrs):
        try:
            credentials = {
                'email': attrs.get('email'),
                'password': attrs.get('password')
            }
            
            user = User.objects.get(email=credentials['email'])
            if user.check_password(credentials['password']):
                if not user.is_active:
                    raise exceptions.AuthenticationFailed('El usuario no está activo')
                update_last_login(None, user)
            else:
                raise exceptions.AuthenticationFailed('Contraseña incorrecta')
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Usuario no encontrado')
        
        refresh = RefreshToken.for_user(user)
        
        return {'access': str(refresh.access_token), 'refresh': str(refresh), 'message': 'Inicio de sesión exitoso'}