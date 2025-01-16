from typing import List
from ninja.pagination import paginate, PageNumberPagination
from ninja import Query, Router
from django.shortcuts import get_object_or_404
from .models import Cliente

from .schemas import ClienteFilter, ClienteList, ClienteInPost, ClienteInPut, ClienteOut

router = Router(tags=['CLIENTE'])

@router.get('cliente/', response=List[ClienteList])
@paginate(PageNumberPagination, page_size=100)
def listar(request, filters: ClienteFilter = Query(...)):
    response = Cliente.objects.all()
    response = filters.filter(response)
    return response


@router.get('cliente/{int:id}', response=ClienteOut)
def listar_consultar(request, id: int):
    response = get_object_or_404(Cliente, id=id)
    return response

@router.post('cliente', response=ClienteOut)
def cliente_criar(request, payload: ClienteInPost):
    response = Cliente.objects.create(**payload.dict())
    return response


@router.put('cliente/{int:id}', response=ClienteOut)
def cliente_autalizar(request, id: int, payload: ClienteInPut):
    cliente = get_object_or_404(Cliente, id = id)
    for attr, value in payload.dict().items():
        setattr(cliente, attr, value)
    cliente.save()
    return cliente
    
    
@router.delete('cliente/{int:id}')
def cliente_deletar(request, id: int):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return {"sucess": True, "message": "Cliente deletado com sucesso"}

