from .models import *
from .serializer import *

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

#Funciones para los vinilos

@api_view(['GET'])
@permission_classes([AllowAny])
def get_products(request):
    if request.method == 'GET':
        products = Vinyl.objects.all()
        serializer = VinylSerializer(products, many=True)
        return Response({"Vinyls": serializer.data, "message": 'Lista generada correctamente', "status":200})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_product(request):
    if request.method == 'POST':
        data = request.data if request.content_type == 'application/json' else request.POST.dict()
        serializer = VinylSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Vinyl": serializer.data, "message": 'Producto creado correctamente', "status":201})
        return Response({"message": 'Error al crear producto', "status":400})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_product(request, pk):
    if request.method == 'GET':
        try:
            product = Vinyl.objects.get(pk=pk)
            serializer = VinylSerializer(product)
            return Response({"Vinyl": serializer.data, "message": 'Producto encontrado', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Producto no encontrado', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_product(request, pk):
    if request.method == 'PUT':
        try:
            product = Vinyl.objects.get(pk=pk)
            data = request.data if request.content_type == 'application/json' else request.POST.dict()
            data.pop('id', None)
            serializer = VinylSerializer(product, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Vinyl": serializer.data, "message": 'Producto actualizado correctamente', "status":200})
            return Response({"message": 'Error al actualizar producto', "status":400})
        except ObjectDoesNotExist:
            return Response({"message": 'Producto no encontrado', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_product(request, pk):
    if request.method == 'DELETE':
        try:
            product = Vinyl.objects.get(pk=pk)
            product.delete()
            return Response({"message": 'Producto eliminado correctamente', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Producto no encontrado', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})


# Funciones para las canciones de los vinilos

@api_view(['GET'])
@permission_classes([AllowAny])
def get_songs(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response({"Songs": serializer.data, "message": 'Lista generada correctamente', "status":200})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_song(request):
    if request.method == 'POST':
        data = request.data if request.content_type == 'application/json' else request.POST.dict()
        serializer = SongSerializer(data=data)
        if Song.objects.filter(title=data['title']).exists():
            return Response({"message": 'La canción ya existe', "status":400})
        if serializer.is_valid():
            serializer.save()
            return Response({"Song": serializer.data, "message": 'Canción creada correctamente', "status":201})
        return Response({"message": 'Error al crear canción', "status":400})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_song(request, pk):
    if request.method == 'GET':
        try:
            song = Song.objects.get(pk=pk)
            serializer = SongSerializer(song)
            return Response({"Song": serializer.data, "message": 'Canción encontrada', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Canción no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_song(request, pk):
    if request.method == 'PUT':
        try:
            song = Song.objects.get(pk=pk)
            data = request.data if request.content_type == 'application/json' else request.POST.dict()
            data.pop('id', None)
            serializer = SongSerializer(song, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Song": serializer.data, "message": 'Canción actualizada correctamente', "status":200})
            return Response({"message": 'Error al actualizar canción', "status":400})
        except ObjectDoesNotExist:
            return Response({"message": 'Canción no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_song(request, pk):
    if request.method == 'DELETE':
        try:
            song = Song.objects.get(pk=pk)
            song.delete()
            return Response({"message": 'Canción eliminada correctamente', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Canción no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

# Funciones para la categoría de los vinilos

@api_view(['GET'])
@permission_classes([AllowAny])
def get_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"Categories": serializer.data, "message": 'Lista generada correctamente', "status":200})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_category(request):
    if request.method == 'POST':
        data = request.data if request.content_type == 'application/json' else request.POST.dict()
        serializer = CategorySerializer(data=data)
        if Category.objects.filter(name=data['name']).exists():
            return Response({"message": 'La categoría ya existe', "status":400})
        if serializer.is_valid():
            serializer.save()
            return Response({"Category": serializer.data, "message": 'Categoría creada correctamente', "status":201})
        return Response({"message": 'Error al crear categoría', "status":400})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_category(request, pk):
    if request.method == 'GET':
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response({"Category": serializer.data, "message": 'Categoría encontrada', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Categoría no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_category(request, pk):
    if request.method == 'PUT':
        try:
            category = Category.objects.get(pk=pk)
            data = request.data if request.content_type == 'application/json' else request.POST.dict()
            data.pop('id', None)
            serializer = CategorySerializer(category, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Category": serializer.data, "message": 'Categoría actualizada correctamente', "status":200})
            return Response({"message": 'Error al actualizar categoría', "status":400})
        except ObjectDoesNotExist:
            return Response({"message": 'Categoría no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_category(request, pk):
    if request.method == 'DELETE':
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({"message": 'Categoría eliminada correctamente', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Categoría no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

# Funciones para la relación entre vinilos y categorías

@api_view(['GET'])
@permission_classes([AllowAny])
def get_vinyl_categories(request):
    if request.method == 'GET':
        vinyl_categories = VinylCategory.objects.all()
        serializer = VinylCategorySerializer(vinyl_categories, many=True)
        return Response({"VinylCategories": serializer.data, "message": 'Lista generada correctamente', "status":200})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_vinyl_category(request):
    if request.method == 'POST':
        data = request.data if request.content_type == 'application/json' else request.POST.dict()
        serializer = VinylCategorySerializer(data=data)
        if VinylCategory.objects.filter(vinyl=data['vinyl'], category=data['category']).exists():
            return Response({"message": 'La relación ya existe', "status":400})
        if serializer.is_valid():
            serializer.save()
            return Response({"VinylCategory": serializer.data, "message": 'Relación creada correctamente', "status":201})
        return Response({"message": 'Error al crear relación', "status":400})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_vinyl_category(request, pk):
    if request.method == 'GET':
        try:
            vinyl_category = VinylCategory.objects.get(pk=pk)
            serializer = VinylCategorySerializer(vinyl_category)
            return Response({"VinylCategory": serializer.data, "message": 'Relación encontrada', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Relación no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_vinyl_category(request, pk):
    if request.method == 'PUT':
        try:
            vinyl_category = VinylCategory.objects.get(pk=pk)
            data = request.data if request.content_type == 'application/json' else request.POST.dict()
            data.pop('id', None)
            serializer = VinylCategorySerializer(vinyl_category, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"VinylCategory": serializer.data, "message": 'Relación actualizada correctamente', "status":200})
            return Response({"message": 'Error al actualizar relación', "status":400})
        except ObjectDoesNotExist:
            return Response({"message": 'Relación no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_vinyl_category(request, pk):
    if request.method == 'DELETE':
        try:
            vinyl_category = VinylCategory.objects.get(pk=pk)
            vinyl_category.delete()
            return Response({"message": 'Relación eliminada correctamente', "status":200})
        except ObjectDoesNotExist:
            return Response({"message": 'Relación no encontrada', "status":404})
    return Response({"message": 'Método incorrecto', "status":400})
