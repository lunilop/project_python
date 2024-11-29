# # __all__ = ["orders_router"]

# # from fastapi import APIRouter
# # from pydantic_mongo import PydanticObjectId

# # from ..__common_deps import QueryParams, QueryParamsDependency
# # from ..models import Order, UpdationProduct
# # from ..services import (
# #     OrdersServiceDependency,
# #     ProductsServiceDependency,
# #     SecurityDependency,
# # )


# # orders_router = APIRouter(prefix="/orders", tags=["Orders"])


# # @orders_router.get("/get_all")
# # def get_all_orders(
# #     orders: OrdersServiceDependency,
# #     security: SecurityDependency,
# #     params: QueryParamsDependency,
# # ):
# #     security.is_admin
# #     return orders.get_all(params)


# # @orders_router.get("/get_by_seller/{id}")
# # def get_orders_by_seller_id(
# #     id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency
# # ):
# #     auth_user_id = security.auth_user_id
# #     assert (
# #         auth_user_id == id or security.auth_user_role == "admin"
# #     ), "User does not have access to this orders"

# #     params = QueryParams(filter=f"seller_id={id}")
# #     return orders.get_all(params)


# # @orders_router.get("/get_by_customer/{id}")
# # def get_orders_by_customer_id(
# #     id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency
# # ):
# #     auth_user_id = security.auth_user_id
# #     assert (
# #         auth_user_id == id or security.auth_user_role == "admin"
# #     ), "User does not have access to this orders"

# #     params = QueryParams(filter=f"custommer_id={id}")
# #     return orders.get_all(params)


# # @orders_router.get("/get_by_product/{id}")
# # def get_orders_by_product_id(
# #     id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency
# # ):
# #     auth_user_id = security.auth_user_id if security.auth_user_role != "admin" else None
# #     return orders.get_one(id, authorized_user_id=auth_user_id)


# # @orders_router.post("/")
# # def create_order(
# #     order: Order,
# #     orders: OrdersServiceDependency,
# #     products: ProductsServiceDependency,
# #     security: SecurityDependency,
# # ):
# #     security.is_customer_or_raise
# #     product = products.get_one(order.product_id)
# #     assert product.get("quantity", 0) >= order.quantity, "Product is out of stock"
# #     products.update_one(
# #         order.product_id,
# #         UpdationProduct(quantity=product["quantity"] - order.quantity),
# #     )
# #     result = orders.create_one(order)
# #     if result:
# #         return {"result message": f"Order created with id: {result}"}


# from fastapi import APIRouter, Depends, HTTPException, status
# from pydantic import BaseModel
# from typing import List
# from ..services.orders import OrdersService, OrdersServiceDependency
# from ..services.promotions import PromotionsService, PromotionsServiceDependency
# from ..services.security import SecurityService, SecurityDependency

# class OrderCreate(BaseModel):
#     user_id: str
#     products: List[str]
#     total_price: float

# orders_router = APIRouter(prefix="/orders", tags=["Orders"])

# @orders_router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_order(
#     order: OrderCreate,
#     security_service: SecurityService = Depends(SecurityDependency),
#     orders_service: OrdersService = Depends(OrdersServiceDependency),
#     promotions_service: PromotionsService = Depends(PromotionsServiceDependency)
# ):
#     security_service.is_customer_or_raise()
    
#     total_price = 0
#     for product_id in order.products:
#         product = await promotions_service.get_product_with_discount(product_id)
#         total_price += product["discounted_price"]
    
#     order.total_price = total_price
#     order_id = orders_service.create_one(order)
#     if order_id:
#         return {"msg": "Order created successfully", "id": order_id}
#     else:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order creation failed")  