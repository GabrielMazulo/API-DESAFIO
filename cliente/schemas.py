from ninja import Schema, ModelSchema, FilterSchema, Field


class ClienteFilter(FilterSchema):
    cliente_id: int = Field(None, q='id__iexact', description='ID do cliente')
    nome: str = Field(None, q='nome__istartswith', description='Nome')


class ClienteList(Schema):
    id: int = Field(..., description='ID do cliente')
    nome: str = Field(..., description='Nome')
    pedido_cliente: str = Field(..., description='Pedido Cliente')


class ClienteOut(Schema):
    id: int = Field(..., description='ID do cliente')
    nome: str = Field(..., description='Nome')
    email: str = Field(..., description='Email')
    senha: str = Field(..., description='Senha')
    pedido_cliente: str = Field(..., description='Pedido Cliente')


class ClienteInPost(Schema):
    nome: str = Field(..., description='Nome')
    email: str = Field(..., description='Email')
    senha: str = Field(..., description='Senha')
    pedido_cliente: str = Field(..., description='Pedido Cliente')

class ClienteInPut(ClienteInPost):
    ...
