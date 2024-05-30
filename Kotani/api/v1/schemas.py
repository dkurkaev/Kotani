from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class MeasureSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class GoodsSchema(BaseModel):
    id: int
    name: str
    parent: Optional[int] = None
    icon: Optional[str] = None  # Use str instead of HttpUrl for simplicity
    measure: MeasureSchema
    is_local: bool
    owner: Optional[int] = None

    class Config:
        orm_mode = True
        from_attributes = True

    @classmethod
    def from_orm(cls, obj):
        return cls(
            id=obj.id,
            name=obj.name,
            parent=obj.parent.id if obj.parent else None,
            icon=obj.icon.url if obj.icon else None,  # Convert ImageField to URL
            measure=MeasureSchema.from_orm(obj.measure),  # Nest MeasureSchema
            is_local=obj.is_local,
            owner=obj.owner.id if obj.owner else None,
        )

class GoodsDetail(BaseModel):
    id: int
    good: str

class RecipeDetailSchema(BaseModel):
    id: int
    name: str
    icon: str
    description: str
    group: str  # Assuming group should be a string. If it should be an int, change this to int.
    cooking_time: str
    goods: List[GoodsDetail]


class RecipesGroupSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


"""
class RecipesSchema(BaseModel):
    id: int
    name: str
    icon: Optional[str] = None  # Use str instead of HttpUrl for simplicity
    description: str
    group: int
    is_local: bool

    class Config:
        orm_mode = True
        from_attributes = True

    @classmethod
    def from_orm(cls, obj):
        return cls(
            id=obj.id,
            name=obj.name,
            icon=obj.icon.url if obj.icon else None,  # Convert ImageField to URL
            description=obj.description,
            group=obj.group.id,  # Convert ForeignKey to integer
            is_local=obj.is_local,
        )
"""


class RecipeGoodsSchema(BaseModel):
    # goods: GoodsSchema
    goods_id: int
    count: float

    class Config:
        orm_mode = True
        from_attributes = True


class RecipeGoodsResponseSchema(BaseModel):
    goods: GoodsSchema
    count: float

    class Config:
        orm_mode = True
        from_attributes = True


class RecipeCreateSchema(BaseModel):
    name: str
    icon: Optional[str] = None  # Use str instead of HttpUrl for simplicity
    description: str
    group: int
    is_local: bool
    cooking_time_max: int  # Include the required field
    cooking_time_min: Optional[int] = None  # Include the optional field
    goods: Optional[List[RecipeGoodsSchema]] = None  # Make goods optional

    class Config:
        orm_mode = True
        from_attributes = True

    class Config:
        orm_mode = True
        from_attributes = True


class RecipeUpdateSchema(BaseModel):
    name: Optional[str] = None
    icon: Optional[str] = None
    description: Optional[str] = None
    group: Optional[int] = None
    is_local: Optional[bool] = None
    cooking_time_max: Optional[int] = None
    cooking_time_min: Optional[int] = None
    goods: Optional[List[RecipeGoodsSchema]] = None  # Allow updating goods

    class Config:
        orm_mode = True
        from_attributes = True


class RecipesSchema(BaseModel):
    id: int
    name: str
    icon: Optional[str] = None  # Use str instead of HttpUrl for simplicity
    description: str
    group: int
    is_local: bool
    goods: List[RecipeGoodsResponseSchema]  # Add the nested schema here

    class Config:
        orm_mode = True
        from_attributes = True

    @classmethod
    def from_orm(cls, obj):
        return cls(
            id=obj.id,
            name=obj.name,
            icon=obj.icon.url if obj.icon else None,  # Convert ImageField to URL
            description=obj.description,
            group=obj.group.id,  # Convert ForeignKey to integer
            is_local=obj.is_local,
            goods=[
                RecipeGoodsResponseSchema(
                    goods=GoodsSchema.from_orm(recipe_goods.goods),
                    count=recipe_goods.count
                ) for recipe_goods in obj.recipe_goods.all()
            ] if hasattr(obj, 'recipe_goods') else []
        )


#class RecipesBatchCreateSchema(BaseModel):
#    recipes: List[RecipeCreateSchema]


#class RecipesBatchUpdateSchema(BaseModel):
#    recipes: List[RecipeUpdateSchema]

class RecipesBatchCreateSchema(BaseModel):
    name: str
    icon: Optional[str]
    description: str
    group: int
    is_local: bool
    cooking_time_max: int
    cooking_time_min: Optional[int]
    goods: Optional[List[RecipeGoodsSchema]]

    class Config:
        orm_mode = True
        from_attributes = True


class RecipesBatchUpdateSchema(BaseModel):
    id: int
    name: Optional[str]
    icon: Optional[str]
    description: Optional[str]
    group: Optional[int]
    is_local: Optional[bool]
    cooking_time_max: Optional[int]
    cooking_time_min: Optional[int]
    goods: Optional[List[RecipeGoodsSchema]]

    class Config:
        orm_mode = True
        from_attributes = True



class FamiliesSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class FamilyMembersSchema(BaseModel):
    id: int
    family: int
    user: int
    is_chef: bool

    class Config:
        orm_mode = True
        from_attributes = True


class FamilyRecipesSchema(BaseModel):
    id: int
    family: int
    recipe: int
    add_date: Optional[datetime] = None
    is_active: bool
    chef: Optional[int] = None

    class Config:
        orm_mode = True
        from_attributes = True


class FamilyGoodsInStockSchema(BaseModel):
    id: int
    family: int
    goods: int
    count: float
    change_date: datetime
    change_user: int

    class Config:
        orm_mode = True
        from_attributes = True
