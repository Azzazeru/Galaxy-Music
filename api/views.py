from rest_framework import viewsets , generics

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view , authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status


from django.shortcuts import get_object_or_404

from .models import *
from .serializer import *


class SelloDiscograficoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SelloDiscografico.objects.all()
    serializer_class = SelloDiscograficoSerializer

class GeneroMusicalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GeneroMusical.objects.all()
    serializer_class = GeneroMusicalSerializer

class ArtistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class DetalleDiscoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleDisco.objects.all()
    serializer_class = DetalleDiscoSerializer

class CancionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

class DiscoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Disco.objects.all()
    serializer_class = DiscoSerializer

class TipoInstrumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoInstrumento.objects.all()
    serializer_class = TipoInstrumentoSerializer

class MarcaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class DetalleInstrumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleInstrumento.objects.all()
    serializer_class = DetalleInstrumentoSerializer

class InstrumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer

# @api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        user = self.request.user
        return Producto.objects.filter(owner=user)

@api_view(['POST'])
def login(request):

    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"Error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"Token": token.key, "User": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, "user":serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):

    # print(request.user)
    serializer = UserSerializer(instance = request.user)

    # return Response("You are login with {}".format(request.user.username), status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)