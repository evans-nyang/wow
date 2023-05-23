from fastapi import APIRouter

from app.services.product_service import ProductService

router = APIRouter()
product_service = ProductService()


@router.get("/products")
def get_products():
    products = product_service.get_all_products()
    return {"products": products}


@router.get("/products/{product_id}")
def get_product(product_id: int):
    product = product_service.get_product_by_id(product_id)
    if product:
        return product
    return {"error": "product not found"}


@router.post("/products")
def create_product(product_data: dict):
    product = product_service.create_product(product_data)
    return product


@router.put("/products/{product_id}")
def update_product(product_id: int, updated_data: dict):
    product = product_service.update_product(product_id, updated_data)
    if product:
        return product
    return {"error": "product not found"}


@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    product_service.delete_product(product_id)
    return {"message": "product deleted"}
