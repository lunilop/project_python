# __all__ = ["ProductsServiceDependency", "ProductsService"]

# from typing import Annotated
# from datetime import datetime

# from fastapi import Depends, HTTPException, status
# from pydantic_mongo import PydanticObjectId

# from ..config import COLLECTIONS, db
# from ..models import Product, StoredProduct, UpdationProduct
# from ..__common_deps import QueryParamsDependency
# from ..services.promotions import PromotionsServiceDependency


# class ProductsService:
#     assert (collection_name := "products") in COLLECTIONS
#     collection = db[collection_name]

#     @classmethod
#     def create_one(cls, product: Product):
#         # if product.promotion_id and not cls.is_promotion_active(product.promotion_id):
#         #     raise HTTPException(
#         #         status_code=status.HTTP_400_BAD_REQUEST, detail="Promotion is not active"
#         #     )
#         # insertion_product = product.model_dump(exclude_unset=True)
#         # result = cls.collection.insert_one(insertion_product)
#         insertion_product = product.model_dump(exclude_unset=True)
#         result = cls.collection.insert_one(insertion_product)
#         if result:
#             return str(result.inserted_id)
#         return None

#     # @classmethod
#     # def is_promotion_active(cls, promotion_id: PydanticObjectId):
#     #     promotion = db.promotions.find_one({"_id": promotion_id})
#     #     if promotion:
#     #         current_date = datetime.now()
#     #         return promotion["start_date"] <= current_date <= promotion["end_date"]
#     #     return False

#     @classmethod
#     def get_all(cls, params: QueryParamsDependency):
#         return [
#             StoredProduct.model_validate(product).model_dump()
#             for product in params.query_collection(cls.collection)
#         ]

#     @classmethod
#     def get_one(cls, id: PydanticObjectId):
#         if db_product := cls.collection.find_one({"_id": id}):
#             return StoredProduct.model_validate(db_product).model_dump()
#         #if not db_product:
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
#             )
        
#         # product_data = StoredProduct.model_validate(db_product).model_dump()

#         # # Verifica la promoción, si existe
#         # if product_data.get("promotion_id"):
#         #     promotion = PromotionsServiceDependency.is_promotion_active(product_data["promotion_id"])
#         #     if promotion:
#         #         # Aplica el descuento y agrega el porcentaje de descuento
#         #         product_data["price_with_discount"] = product_data["price"] * (1 - promotion["discount_percentage"] / 100)
#         #         product_data["promotion_percentage"] = promotion["discount_percentage"]
#         #     else:
#         #         # Si la promoción no está activa, no incluimos el precio con descuento
#         #         product_data["price_with_discount"] = product_data["price"]
#         #         product_data["promotion_percentage"] = 0
        
#         # return product_data

#     @classmethod
#     def update_one(cls, id: PydanticObjectId, product: UpdationProduct):
#         document = cls.collection.find_one_and_update(
#             {"_id": id},
#             {"$set": product.model_dump()},
#             return_document=True,
#         )
#         if document:
#             return StoredProduct.model_validate(document).model_dump()
#         else:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

#     @classmethod
#     def delete_one(cls, id: PydanticObjectId):
#         document = cls.collection.find_one_and_delete({"_id": id})
#         if document:
#             return StoredProduct.model_validate(document).model_dump()
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
#             )

# ProductsServiceDependency = Annotated[ProductsService, Depends()]

__all__ = ["ProductsServiceDependency", "ProductsService"]

from typing import Annotated

from fastapi import Depends, HTTPException, status      # defininedo la dependencia le podemos pasar a nuestro controlador 
from pydantic_mongo import PydanticObjectId

from ..config import COLLECTIONS, db
from ..models import Product, StoredProduct, UpdationProduct
from ..__common_deps import QueryParamsDependency


class ProductsService:                                               # := asigna dentro de otra exprecion 
    assert (collection_name := "products") in COLLECTIONS       # me aseguro que me refiero a esta coleccion 
    collection = db[collection_name]            # atibuto de la clase, estable que tengo acceso a la coleccion

    @classmethod
    def create_one(cls, product: Product):
        insertion_product = product.model_dump(exclude_unset=True)
        result = cls.collection.insert_one(insertion_product)
        if result:
            return str(result.inserted_id)
        return None

    @classmethod
    def get_all(cls, params: QueryParamsDependency):
        return [
            StoredProduct.model_validate(product).model_dump()
            for product in params.query_collection(cls.collection)
        ]

    @classmethod
    def get_one(cls, id: PydanticObjectId):
        if db_product := cls.collection.find_one({"_id": id}):
            return StoredProduct.model_validate(db_product).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )

    @classmethod
    def update_one(cls, id: PydanticObjectId, product: UpdationProduct):
        document = cls.collection.find_one_and_update(
            {"_id": id},
            {"$set": product.model_dump()},
            return_document=True,
        )

        if document:
            return StoredProduct.model_validate(document).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )

    @classmethod
    def delete_one(cls, id: PydanticObjectId):
        document = cls.collection.find_one_and_delete({"_id": id})
        if document:
            return StoredProduct.model_validate(document).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )


ProductsServiceDependency = Annotated[ProductsService, Depends()]
