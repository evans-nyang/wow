from fastapi import APIRouter

from app.services.order_service import OrderService

router = APIRouter()
order_service = OrderService()


@router.get("/orders")
def get_orders():
    orders = order_service.get_all_orders()
    return {"orders": orders}


@router.get("/orders/{order_id}")
def get_order(order_id: int):
    order = order_service.get_order_by_id(order_id)
    if order:
        return order
    return {"error": "order not found"}


@router.post("/orders")
def create_order(order_data: dict):
    order = order_service.create_order(order_data)
    return order


@router.put("/orders/{order_id}")
def update_order(order_id: int, updated_data: dict):
    order = order_service.update_order(order_id, updated_data)
    if order:
        return order
    return {"error": "order not found"}


@router.delete("/orders/{order_id}")
def delete_order(order_id: int):
    order_service.delete_order(order_id)
    return {"message": "order deleted"}
