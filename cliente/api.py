
from ninja import NinjaAPI, Schema, ModelSchema
from .models import Cliente
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict


api_v1 = NinjaAPI(version="1.0.0")

@api_v1.get('cliente/')
def listar(request):
    cliente = Cliente.objects.all()
    response = [{'id': i.id, 'nome': i.nome,'email': i.email, 'senha': i.senha, 'pedido_cliente': i.pedido_cliente}for i in cliente] 
    return response


@api_v1.get('cliente_consulta/')
def listar_consultar(request, id: int = 1):
     cliente = get_object_or_404(Cliente, id=id)
     return model_to_dict(cliente)


class ClienteSchema(ModelSchema):
    class Config:
        model = Cliente
        model_fields = ['id','nome', 'email', 'senha', 'pedido_cliente']


@api_v1.post('cliente', response=ClienteSchema)
def cliente_criar(request, cliente: ClienteSchema):
    l1 = cliente.dict()
    novo_cliente = Cliente(**l1)
    novo_cliente.save()
    return cliente


@api_v1.put('cliente/{id}', response=ClienteSchema)
def cliente_autalizar(request, id: int, dado_atualizados: ClienteSchema):
    cliente = get_object_or_404(Cliente, id = id)
    for attr, value in dado_atualizados.dict().items():
        setattr(cliente, attr, value)
    cliente.save()
    return model_to_dict(cliente)
    
    
@api_v1.delete('cliente/{id}')
def cliente_deletar(request, id: int):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return {"sucess": True, "message": "Cliente deletado com sucesso"}

