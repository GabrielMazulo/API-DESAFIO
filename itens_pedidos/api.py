
from ninja import NinjaAPI, Schema, ModelSchema
from .models import Itens_pedidos
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

api_v3 = NinjaAPI(version="3.0.0")

@api_v3.get('itens_pedidos/')
def listar(request):
    itens_pedidos = Itens_pedidos.objects.all()
    response = [{'id': i.id, 'nome_itens':i.nome_itens,'descricao': i.descricao, 'preco': i.preco, 'categoria': i.categoria}for i in itens_pedidos] 
    return response



@api_v3.get('itens_pedidos_consulta/')
def consultar_itens_pedidos(request, id: int = 1):
     itens_pedidos = get_object_or_404(Itens_pedidos, id=id)
     return model_to_dict(itens_pedidos)




class Itens_pedidosSchema(ModelSchema):
    class Config:
        model = Itens_pedidos
        model_fields = ['id', 'nome_itens', 'descricao', 'preco', 'categoria']



@api_v3.post('itens_pedidos', response=Itens_pedidosSchema)
def itens_pedidos_criar(request, itens_pedidos: Itens_pedidosSchema):
    l1 = itens_pedidos.dict()
    novo_itens_pedidos = Itens_pedidos(**l1)
    novo_itens_pedidos.save()
    return itens_pedidos



@api_v3.put('itens_pedidos/{id}', response=Itens_pedidosSchema)
def itens_pedidos_autalizar(request, id: int, dado_atualizados: Itens_pedidosSchema):
    itens_pedidos= get_object_or_404(Itens_pedidos, id = id)
    for attr, value in dado_atualizados.dict().items():
        setattr(itens_pedidos, attr, value)
    itens_pedidos.save()
    return model_to_dict(itens_pedidos)
    


@api_v3.delete('itens_pedidos/{id}')
def itens_pedidos_deletar(request, id: int):
    itens_pedidos = get_object_or_404(Itens_pedidos, id=id)
    itens_pedidos.delete()
    return {"sucess": True, "message": "Item deletado com sucesso"}



