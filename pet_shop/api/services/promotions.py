# # __all__ = ["PromotionServiceDependency", "PromotionService"]

# # from typing import Annotated

# # from fastapi import Depends, HTTPException, status      # defininedo la dependencia le podemos pasar a nuestro controlador 
# # from pydantic_mongo import PydanticObjectId

# # from ..config import COLLECTIONS, db
# # from ..models import Promotion, StoredPromotion
# # from ..__common_deps import QueryParamsDependency

# # from datetime import datetime


# # class PromotionService:
# #     @staticmethod
# #     async def create_promotion(promotion_data: dict):
# #         result = await db["promotions"].insert_one(promotion_data)
# #         return str(result.inserted_id)

# #     @staticmethod
# #     async def validate_promotion(code: str):
# #         promotion = await db["promotions"].find_one({"code": code})
# #         if promotion and datetime.strptime(promotion["expiration_date"], "%Y-%m-%d") > datetime.now():
# #             return Promotion(**promotion)
# #         return None
    

# # ProductsServiceDependency = Annotated[PromotionService, Depends()]

# __all__ = ["PromotionsServiceDependency", "PromotionsService"]

# from datetime import datetime
# from typing import Annotated
# from fastapi import Depends, HTTPException, status
# from pydantic_mongo import PydanticObjectId

# from ..config import COLLECTIONS, db, logger
# from ..models import Promotion, StoredPromotion, UpdationPromotion
# from ..__common_deps import QueryParamsDependency

# class PromotionsService:
#     assert (collection_name := "promotion") in COLLECTIONS
#     collection = db[collection_name]

#     @classmethod
#     def create_one(cls, promotion: Promotion):
#         if promotion.end_date < promotion.start_date:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="End date cannot be before start date."
#             )

#         insertion_data = promotion.model_dump(exclude_unset=True)
#         result = cls.collection.insert_one(insertion_data)
#         if result:
#             logger.info("Promotion created successfully.")
#             return str(result.inserted_id)
#         return None

#     @classmethod
#     def get_all(cls, params: QueryParamsDependency):
#         return [
#             StoredPromotion.model_validate(promo).model_dump()
#             for promo in params.query_collection(cls.collection)
#         ]

#     @classmethod
#     def get_one(cls, id: PydanticObjectId):
#         if db_promotion := cls.collection.find_one({"_id": id}):
#             return StoredPromotion.model_validate(db_promotion).model_dump()
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found"
#             )

#     @classmethod
#     def update_one(cls, id: PydanticObjectId, promotion: UpdationPromotion):
#         if promotion.expiration_date and datetime.strptime(promotion.expiration_date, "%Y-%m-%d") < datetime.now():
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Expiration date cannot be in the past."
#             )

#         document = cls.collection.find_one_and_update(
#             {"_id": id},
#             {"$set": promotion.model_dump(exclude_unset=True)},
#             return_document=True,
#         )

#         if document:
#             logger.info(f"Promotion with ID {id} updated.")
#             return StoredPromotion.model_validate(document).model_dump()
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found"
#             )

#     @classmethod
#     def delete_one(cls, id: PydanticObjectId):
#         document = cls.collection.find_one_and_delete({"_id": id})
#         if document:
#             logger.info(f"Promotion with ID {id} deleted.")
#             return StoredPromotion.model_validate(document).model_dump()
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found"
#             )

#     @classmethod
#     def is_promotion_active(cls, promotion_id: PydanticObjectId):
#         promotion = cls.collection.find_one({"_id": promotion_id})
#         if not promotion:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found"
#             )
        
#         current_date = datetime.now()
#         start_date = promotion["start_date"]
#         end_date = promotion["end_date"]
        
#         if start_date <= current_date <= end_date:
#             return StoredPromotion.model_validate(promotion).model_dump()
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Promotion is not active."
#             )

# PromotionsServiceDependency = Annotated[PromotionsService, Depends()]