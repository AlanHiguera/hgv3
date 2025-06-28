from rest_framework import viewsets, permissions
from api.models import Producto, Usuario, Administrador, Venta, ProductoDeseado, tipoCategoria, Carrito, Tienda, SeguimientoTienda
from api.serializers import ProductoSerializer, UsuarioSerializer, UserSerializer, AdministradorSerializer, VentaSerializer, ProductoDeseadoSerializer, tipoCategoriaSerializer, CarritoSerializer, TiendaSerializer, SeguimientoTiendaSerializer
from rest_framework import status,views, response
from rest_framework import authentication
from django.contrib.auth.models import User
from django.contrib.auth import logout ,authenticate, login 
from rest_framework.authtoken.models import Token

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.BasicAuthentication]
    

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.BasicAuthentication,]

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.BasicAuthentication,]

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.BasicAuthentication,]

class ProductoDeseadoViewSet(viewsets.ModelViewSet):
    queryset = ProductoDeseado.objects.all()
    serializer_class = ProductoDeseadoSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.BasicAuthentication,]

class tipoCategoriaViewSet(viewsets.ModelViewSet):
    queryset = tipoCategoria.objects.all()
    serializer_class = tipoCategoriaSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.BasicAuthentication,]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
    authentication_classes = [authentication.BasicAuthentication,]

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()  # Assuming you want to list products in the cart
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication,]

class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()  # Assuming you want to list products in the store
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.BasicAuthentication,]

class SeguimientoTiendaViewSet(viewsets.ModelViewSet):
    queryset = SeguimientoTienda.objects.all()  # Assuming you want to track products in the store
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.BasicAuthentication,]

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        username2= request.data.get('username', None)
        password2 = request.data.get('password', None)
        if username2 is None or password2 is None:
            return response.Response({'message': 'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
        user2 = authenticate(username=username2, password=password2)
        if not user2:
            return response.Response({'message': 'Usuario o Contraseña incorrecto !!!! '},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user2)
        # Si es correcto añadimos a la request la información de sesión
        if user2:
            # para loguearse una sola vez
            # login(request, user)
            return response.Response({'message':'usuario y contraseña correctos!!!!'},status=status.HTTP_200_OK)
            #return response.Response({'token': token.key}, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return response.Response(status=status.HTTP_404_NOT_FOUND)        

class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):        
        request.user.auth_token.delete()
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return response.Response({'message':'Sessión Cerrada y Token Eliminado !!!!'},status=status.HTTP_200_OK)

#%@api_view(['POST'])
def AgAlCarrito(request):
    # Obtén los datos del request (enviados desde Postman)
    usuario_id = request.data.get('usuario_id')
    producto_id = request.data.get('producto_id')
    unidades = request.data.get('unidades', 1)  # Default: 1

    # Valida que existan el usuario y el producto
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
        producto = Producto.objects.get(pk=producto_id)
    except (Usuario.DoesNotExist, Producto.DoesNotExist):
        return Response(
            {'error': 'Usuario o Producto no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    # Crea o actualiza el item en el carrito
    item_carrito, creado = Carrito.objects.get_or_create(
        usuario=usuario,
        producto=producto,
        defaults={'unidades': unidades}
    )

    if not creado:
        item_carrito.unidades += unidades
        item_carrito.save()

    return Response(
        {'mensaje': 'Producto agregado al carrito', 'item_id': item_carrito.id},
        status=status.HTTP_201_CREATED
    )