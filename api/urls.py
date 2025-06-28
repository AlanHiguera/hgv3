from rest_framework import routers
from api.views import ProductoViewSet, UsuarioViewSet, UserViewSet, LogoutView , LoginView, AdministradorViewSet, VentaViewSet, ProductoDeseadoViewSet, tipoCategoriaViewSet, CarritoViewSet, TiendaViewSet, SeguimientoTiendaViewSet, AgAlCarrito
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
router  = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('usuario', UsuarioViewSet)
router.register('administrador', AdministradorViewSet)
router.register('Venta', VentaViewSet)
router.register('productodeseado', ProductoDeseadoViewSet)
router.register('tipocategoria', tipoCategoriaViewSet)
router.register('user', UserViewSet)
router.register('carrito', CarritoViewSet)
router.register('tienda', TiendaViewSet)
router.register('seguimientotienda', SeguimientoTiendaViewSet)


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('api/carrito/agregar/', AgAlCarrito, name='agregar_al_carrito'),
] + router.urls
