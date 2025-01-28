from ninja import NinjaAPI

api_v1 = NinjaAPI(version="1.0.0")

#CLIENTE
api_v1.add_router('', 'cliente.api.router')