# __all__ = ["Order", "StoredOrder"]

# from pydantic import BaseModel, Field, field_validator
# from pydantic_mongo import PydanticObjectId
# from enum import Enum

# class PaymentMethod(str, Enum):
#     transfer = "transfer"
#     cash = "cash"

# class Order(BaseModel):
#     customer_id: PydanticObjectId
#     product_id: PydanticObjectId
#     price: float
#     quantity: int
#     paymenth_method: PaymentMethod =  PaymentMethod.cash 
#     final_price: float
    
#     @field_validator("price", "final_price")
#     def must_be_positive(cls, value):
#         if value < 0:
#             raise ValueError("Value must be positive.")
#         return value
    
#     @field_validator("final_price", pre=True, always=True)
#     def calculate_final_price(cls, final_price, values):
#         price = values.get("price")
#         quantity = values.get("quantity", 1)
#         final_price = price * quantity  # Cálculo básico
#         return final_price

#     @field_validator("quantity")
#     def quantity_must_be_positive(cls, value):
#         if value <= 0:
#             raise ValueError("Quantity must be greater than zero.")
#         return value


# class StoredOrder(Order):
#     id: PydanticObjectId = Field(alias="_id")
    

