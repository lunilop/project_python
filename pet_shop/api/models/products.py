__all__ = ["Product", "StoredProduct", "UpdationProduct"]

from enum import Enum
from pydantic import BaseModel, Field, field_validator
from pydantic_mongo import PydanticObjectId

class Pet_Type(str, Enum):
    dog = "dog"
    cat = "cat"
    fish = "fish"
    bird = "bird"
    smallAnimal = "smallAnimal"
   # reptile = "reptile"

class Category(str, Enum):
    food = "food"
    accessory = "accessory" 
    toy = "toy"
    health = "health"
    hygiene = "hygiene"
    snack = "snack"


class Product(BaseModel):
    employee_id: PydanticObjectId
    name: str
    description: str = Field(default=None)
    pet_type: Pet_Type = Pet_Type.dog
    category: Category = Category.food
    price: float
    quantity: int
    image: str = Field(default=None)
    # promotion_id: PydanticObjectId = Field(default=None)
    
    # @field_validator("price")
    # def price_must_be_positive(cls, value):
    #     if value < 0:
    #         raise ValueError(f"Price must be a positive number.")
    #     return value

    # @field_validator("stock")
    # def stock_must_be_non_negative(cls, value):
    #     if value < 0:
    #         raise ValueError("Stock must be a non-negative integer.")
    #     return value


class UpdationProduct(BaseModel):
    employee_id: PydanticObjectId = Field(default=None)
    name: str = Field(default=None)
    description: str = Field(default=None)
    pet_type: Pet_Type = Field(default=None)
    category: Category = Field(default=None)    
    price: float = Field(default=None)
    quantity: int = Field(default=None)
    image: str = Field(default=None)


class StoredProduct(Product):
    id: PydanticObjectId = Field(alias="_id")
