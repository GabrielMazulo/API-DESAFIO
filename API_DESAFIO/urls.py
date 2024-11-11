
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls')),
    path('itens_pedidos/',include('itens_pedidos.urls')),
    path('pedido/',include('pedido.urls'))
]
