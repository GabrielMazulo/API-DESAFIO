
from ninja import NinjaAPI, Schema, ModelSchema
from .models import Pedido
from pedido.models import Pedido
from cliente.models import Cliente
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from datetime import datetime

api_v2 = NinjaAPI(version="2.0.0")



@api_v2.get('pedido/')
def listar(request):
    pedido = Pedido.objects.all()
    response = [{'id': i.id, 'total':i.total,'status': i.status, 'data_pedido': i.data_pedido}for i in pedido] 
    return response


@api_v2.get('pedido/data/')
def consultar_pedido_por_data(request, data_inicio: str = None, data_fim: str = None):
 if data_inicio:
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
 if data_fim:
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
        pedido = Pedido.objects.all()

 if data_inicio:
        pedido = pedido.filter(data_pedido__gte=data_inicio)
 if data_fim:
        pedido = pedido.filter(data_pedido__lte=data_fim)

 if not pedido:
        return {"message": "Nenhum pedido encontrado para o intervalo de datas fornecido"}

 response = [{'id': i.id, 'total': i.total, 'status': i.status, 'data_pedido': i.data_pedido} for i in pedido]
 return response




@api_v2.get('pedido_consulta/')
def consultar_pedidos(request, id: int = 1):
     pedido = get_object_or_404(Pedido, id=id)
     return model_to_dict(pedido)




@api_v2.get('pedido/status/{status}/')
def consultar_pedidos_por_status(request, status: str):
    pedido = Pedido.objects.filter(status=status)

    if not pedido:
        return {"message": "Nenhum pedido encontrado com esse status"}
    
    response = [{'id': i.id, 'total': i.total, 'status': i.status, 'data_pedido': i.data_pedido, 'cliente_pedido':i.cliente_id} for i in pedido]
    return response



class PedidoSchema(ModelSchema):
    class Config:
        model = Pedido
        model_fields = ['id', 'total','cliente', 'status', 'data_pedido']



@api_v2.post('pedido', response=PedidoSchema)
def pedido_criar(request, pedido: PedidoSchema):
    l1 = pedido.dict()
    novo_pedido = Pedido(**l1)
    novo_pedido.save()
    return pedido



@api_v2.put('pedido/{id}', response=PedidoSchema)
def pedido_autalizar(request, id: int, dado_atualizados: PedidoSchema):
    pedido = get_object_or_404(Pedido, id = id)
    for attr, value in dado_atualizados.dict().items():
        setattr(pedido, attr, value)
    pedido.save()
    return model_to_dict(pedido)
    


@api_v2.delete('pedido/{id}')
def pedido_deletar(request, id: int):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return {"sucess": True, "message": "Pedido deletado com sucesso"}


@api_v2.get('pedidos/cliente/{cliente_id}/')
def listar_pedidos_por_cliente(request, cliente_id: int):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    pedidos = cliente.pedidos_cliente.all()   # Usa o `related_name` definido
    response = [{'id': pedido.id, 'total': pedido.total, 'status': pedido.status, 'data_pedido': pedido.data_pedido} for pedido in pedidos]
    return response

