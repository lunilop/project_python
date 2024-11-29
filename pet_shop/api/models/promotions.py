# __all__ = ["Promotion", "StoredPromotion", "UpdationPromotion"]

# from pydantic import BaseModel, Field, field_validator
# from pydantic_mongo import PydanticObjectId
# from datetime import datetime

# class Promotion(BaseModel):
#     name: str
#     description: str
#     discount_percentage: float = Field(ge=0, le=100)
#     start_date: datetime
#     end_date: datetime
    
#     @field_validator("end_date")
#     def end_date_must_be_after_start_date(cls, end_date, values):
#         if "start_date" in values and end_date <= values["start_date"]:
#             raise ValueError("End date must be after start date.")
#         return end_date

#     @field_validator("discount_percentage")
#     def discount_must_be_valid(cls, value):
#         if value <= 0 or value > 100:
#             raise ValueError("Discount percentage must be between 0 and 100.")
#         return value
    
    
# class UpdationPromotion(BaseModel):
#     seller_id: PydanticObjectId = Field(default=None)
#     code: str = Field(default=None)   
#     discount_percentage: float = Field(default=None)
#     expiration_date: str = Field(default=None)

#     @field_validator("expiration_date", pre=True, always=True)
#     def check_expiration_date(cls, value):
#         if value and value < datetime.now():
#             raise ValueError("Expiration date must be in the future.")
#         return value

# class StoredPromotion(Promotion):
#     id: PydanticObjectId = Field(alias="_id")
