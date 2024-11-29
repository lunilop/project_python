# # from fastapi import APIRouter, Depends, HTTPException, status
# # from pydantic import BaseModel
# # from typing import List
# # from ..services.promotions import PromotionsService, PromotionsServiceDependency
# # from ..services.security import SecurityService, SecurityDependency

# # # Definir los modelos para la creación y actualización de promociones
# # class PromotionCreate(BaseModel):
# #     product_id: str
# #     discount_percentage: float
# #     start_date: str
# #     end_date: str

# # class PromotionUpdate(BaseModel):
# #     discount_percentage: float
# #     start_date: str
# #     end_date: str

# # # Inicializar el router para las promociones
# # promotion_router = APIRouter(prefix="/promotions", tags=["Promotions"])

# # @promotion_router.post("/", status_code=status.HTTP_201_CREATED)
# # async def create_promotion(
# #     promotion: PromotionCreate,
# #     security_service: SecurityService = Depends(SecurityDependency),
# #     promotions_service: PromotionsService = Depends(PromotionsServiceDependency)
# # ):
# #     # Verificar que el usuario tiene el rol adecuado
# #     security_service.is_admin_or_raise

# #     # Crear la promoción
# #     promotion_id = promotions_service.create_one(promotion)
# #     if promotion_id:
# #         return {"msg": "Promotion created successfully", "id": promotion_id}
# #     else:
# #         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Promotion creation failed")

# # @promotion_router.put("/{promotion_id}", status_code=status.HTTP_200_OK)
# # async def update_promotion(
# #     promotion_id: str,
# #     promotion: PromotionUpdate,
# #     security_service: SecurityService = Depends(SecurityDependency),
# #     promotions_service: PromotionsService = Depends(PromotionsServiceDependency)
# # ):
# #     # Verificar que el usuario tiene el rol adecuado
# #     security_service.is_admin_or_raise

# #     # Actualizar la promoción
# #     updated_promotion = promotions_service.update_one(promotion_id, promotion)
# #     if updated_promotion:
# #         return {"msg": "Promotion updated successfully", "promotion": updated_promotion}
# #     else:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")

# # @promotion_router.delete("/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
# # async def delete_promotion(
# #     promotion_id: str,
# #     security_service: SecurityService = Depends(SecurityDependency),
# #     promotions_service: PromotionsService = Depends(PromotionsServiceDependency)
# # ):
# #     # Verificar que el usuario tiene el rol adecuado
# #     security_service.is_admin_or_raise

# #     # Eliminar la promoción
# #     result = promotions_service.delete_one(promotion_id)
# #     if result:
# #         return {"msg": "Promotion deleted successfully"}
# #     else:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")

# from fastapi import APIRouter, Depends, HTTPException, status
# from pydantic import BaseModel
# from typing import List
# from ..services.promotions import PromotionsService, PromotionsServiceDependency
# from ..services.security import SecurityService, SecurityDependency

# # Definir los modelos para la creación y actualización de promociones
# class PromotionCreate(BaseModel):
#     product_id: str
#     discount_percentage: float
#     start_date: str
#     end_date: str

# class PromotionUpdate(BaseModel):
#     discount_percentage: float
#     start_date: str
#     end_date: str

# # Inicializar el router para las promociones
# promotion_router = APIRouter(prefix="/promotions", tags=["Promotions"])

# @promotion_router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_promotion(
#     promotion: PromotionCreate,
#     security_service: SecurityService = Depends(SecurityDependency),
#     promotions_service: PromotionsService = Depends(PromotionsServiceDependency)
# ):
#     # Verificar que el usuario tiene el rol adecuado
#     security_service.is_admin_or_raise

#     # Crear la promoción
#     promotion_id = promotions_service.create_one(promotion)
#     if promotion_id:
#         return {"msg": "Promotion created successfully", "id": promotion_id}
#     else:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Promotion creation failed")

# @promotion_router.put("/{promotion_id}", status_code=status.HTTP_200_OK)
# async def update_promotion(
#     promotion_id: str,
#     promotion: PromotionUpdate,
#     security_service: SecurityService = Depends(SecurityDependency),
#     promotions_service: PromotionsService = Depends(PromotionsServiceDependency)
# ):
#     # Verificar que el usuario tiene el rol adecuado
#     security_service.is_admin_or_raise

#     # Actualizar la promoción
#     updated_promotion = promotions_service.update_one(promotion_id, promotion)
#     if updated_promotion:
#         return {"msg": "Promotion updated successfully", "promotion": updated_promotion}
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")

# @promotion_router.delete("/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_promotion(
#     promotion_id: str,
#     security_service: SecurityService = Depends(SecurityDependency),
#     promotions_service: PromotionsService = Depends(PromotionsServiceDependency)
# ):
#     # Verificar que el usuario tiene el rol adecuado
#     security_service.is_admin_or_raise

#     # Eliminar la promoción
#     result = promotions_service.delete_one(promotion_id)
#     if result:
#         return {"msg": "Promotion deleted successfully"}
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")