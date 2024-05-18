from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Body

from app.models.comment import Comment
from app.models.product import Product
from app.services.products_service import ProductsService

products_router = APIRouter(prefix='/products')
ProductsServiceInj = Annotated[ProductsService, Depends(ProductsService)]


@products_router.get('/')
def get_products(service: ProductsServiceInj):
    return service.get_products()


@products_router.post('/create_product')
def create_product(product: Product, service: ProductsServiceInj) -> Product:
    try:
        return service.create_product(product)
    except:
        raise HTTPException(418, 'Teapot')


@products_router.get('/{product_id}/comments')
def get_comments(product_id: UUID, service: ProductsServiceInj) -> list[Comment]:
    try:
        return service.get_comments(product_id)
    except:
        raise HTTPException(418, 'Teapot')
