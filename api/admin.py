from django.contrib import admin
# Register your models here.
from api.models import Producto, Persona, Usuario, Administrador, Venta, ProductoDeseado, tipoCategoria, Carrito, Tienda, SeguimientoTienda

admin.site.register(Producto)
admin.site.register(Persona)
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Venta)
admin.site.register(ProductoDeseado)
admin.site.register(tipoCategoria)
admin.site.register(Carrito)
admin.site.register(Tienda)
admin.site.register(SeguimientoTienda)