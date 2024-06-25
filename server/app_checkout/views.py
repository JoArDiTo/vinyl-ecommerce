from .models import *
from .serializer import *

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

#METODOS GET, POST, PUT, DELETE PARAR CREDITCARD

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@permission_required('app_checkout.view_creditcard', raise_exception=True)
def get_creditcards(request):
    if request.method == 'GET':
        creditcards = CreditCard.objects.all()
        serializer = CreditCardSerializer(creditcards, many=True)
        return Response({"Credit Cards": serializer.data, "message": 'Lista generada correctamente', "status":200})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@permission_required('app_checkout.add_creditcard', raise_exception=True)
def create_creditcard(request):
    if request.method == 'POST':
        data = request.data if request.content_type == 'application/json' else request.POST.dict()
        serializer = CreditCardSerializer(data=data)
        if CreditCard.objects.filter(number=data['number']).exists():
            return Response({"message": 'El número de tarjeta ya existe', "status":400})
        if serializer.is_valid():
            serializer.save()
            return Response({"Credit Card": serializer.data, "message": 'Tarjeta añadida correctamente', "status":201})
        return Response({"message": 'Datos incorrectos', "status":400})
    return Response({"message": 'Método incorrecto', "status":400})
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@permission_required('app_checkout.change_creditcard', raise_exception=True)
def update_creditcard(request, pk):
    if request.method == 'PUT':
        try:
            creditcard = CreditCard.objects.get(pk=pk)
            data = request.data if request.content_type == 'application/json' else request.POST.dict()
            data.pop('id', None)
            serializer = CreditCardSerializer(creditcard, data=data, partial=True)
            if CreditCard.objects.filter(number=data['number']).exists():
                return Response({"message": 'El número de tarjeta ha actualizar ya existe', "status":400})
            if serializer.is_valid():
                serializer.save()
                return Response({"Credit Card": serializer.data, "message": 'Tarjeta actualizada correctamente', "status":200})
            return Response({"message": 'Error al actualizar la tarjeta', "status":400})
        except ObjectDoesNotExist:
            return Response({"message": 'Tarjeta no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@permission_required('app_checkout.delete_creditcard', raise_exception=True)
def delete_creditcard(request, pk):
    if request.method == 'DELETE':
        try:
            creditcard = CreditCard.objects.get(pk=pk)
            creditcard.delete()
            return Response({"message": 'Tarjeta eliminada correctamente', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Tarjeta no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

#METODOS GET, POST, PUT, DELETE PARA PURCHASE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@permission_required('app_checkout.view_purchase', raise_exception=True)
def get_purchases(request):
    if request.method == 'GET':
        purchases = Purchase.objects.all()
        serializer = PurchaseSerializer(purchases, many=True)
        return Response({"Purchases": serializer.data, "message": 'Lista generada correctamente', "status":200})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@permission_required('app_checkout.add_purchase', raise_exception=True)
def create_purchase(request):
    if request.method == 'POST':
        data = request.data if request.content_type == 'application/json' else request.POST.dict()
        serializer = PurchaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Purchase": serializer.data, "message": 'Compra añadida correctamente', "status":201})
        return Response({"message": 'Datos incorrectos', "status":400})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@permission_required('app_checkout.view_purchase', raise_exception=True)
def get_purchase(request, pk):
    if request.method == 'GET':
        try:
            purchase = Purchase.objects.get(pk=pk)
            serializer = PurchaseSerializer(purchase)
            return Response({"Purchase": serializer.data, "message": 'Compra generada correctamente', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Compra no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@permission_required('app_checkout.change_purchase', raise_exception=True)
def update_purchase(request, pk):
    if request.method == 'PUT':
        try:
            purchase = Purchase.objects.get(pk=pk)
            data = request.data if request.content_type == 'application/json' else request.POST.dict()
            data.pop('id', None)
            serializer = PurchaseSerializer(purchase, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Purchase": serializer.data, "message": 'Compra actualizada correctamente', "status":200})
            return Response({"message": 'Error al actualizar la compra', "status":400})
        except ObjectDoesNotExist:
            return Response({"message": 'Compra no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_purchase(request, pk):
    if request.method == 'DELETE':
        try:
            purchase = Purchase.objects.get(pk=pk)
            purchase.delete()
            return Response({"message": 'Compra eliminada correctamente', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Compra no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})