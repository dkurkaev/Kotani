import logging
from ninja import Router
from .schemas import (
    MeasureSchema, GoodsSchema, RecipesGroupSchema, RecipesSchema, RecipeCreateSchema, RecipeUpdateSchema,
    RecipesBatchCreateSchema, RecipesBatchUpdateSchema,
    FamiliesSchema, FamilyMembersSchema, FamilyRecipesSchema, FamilyGoodsInStockSchema
)
from typing import List
from ...models import Measure, Goods, RecipesGroup, Recipes, Families, FamilyMembers, FamilyRecipes, FamilyGoodsInStock, \
    RecipeGoods

router = Router()
logger = logging.getLogger(__name__)


@router.get("/measures", response=List[MeasureSchema])
def list_measures(request):
    measures = Measure.objects.all()
    return [MeasureSchema.from_orm(measure) for measure in measures]


@router.get("/measures/{measure_id}", response=MeasureSchema)
def get_measure(request, measure_id: int):
    measure = Measure.objects.get(id=measure_id)
    return MeasureSchema.from_orm(measure)


@router.post("/measures", response=MeasureSchema)
def create_measure(request, payload: MeasureSchema):
    measure = Measure.objects.create(**payload.dict())
    return MeasureSchema.from_orm(measure)


@router.put("/measures/{measure_id}", response=MeasureSchema)
def update_measure(request, measure_id: int, payload: MeasureSchema):
    measure = Measure.objects.get(id=measure_id)
    for attr, value in payload.dict().items():
        setattr(measure, attr, value)
    measure.save()
    return MeasureSchema.from_orm(measure)


@router.delete("/measures/{measure_id}")
def delete_measure(request, measure_id: int):
    measure = Measure.objects.get(id=measure_id)
    measure.delete()
    return {"success": True}


@router.get("/goods", response=List[GoodsSchema])
def list_goods(request):
    goods = Goods.objects.all()
    return [GoodsSchema.from_orm(good) for good in goods]


@router.get("/goods/{goods_id}", response=GoodsSchema)
def get_goods(request, goods_id: int):
    good = Goods.objects.get(id=goods_id)
    return GoodsSchema.from_orm(good)


@router.post("/goods", response=GoodsSchema)
def create_goods(request, payload: GoodsSchema):
    good = Goods.objects.create(**payload.dict())
    return GoodsSchema.from_orm(good)


@router.put("/goods/{goods_id}", response=GoodsSchema)
def update_goods(request, goods_id: int, payload: GoodsSchema):
    good = Goods.objects.get(id=goods_id)
    for attr, value in payload.dict().items():
        setattr(good, attr, value)
    good.save()
    return GoodsSchema.from_orm(good)


@router.delete("/goods/{goods_id}")
def delete_goods(request, goods_id: int):
    good = Goods.objects.get(id=goods_id)
    good.delete()
    return {"success": True}


@router.get("/recipes-groups", response=List[RecipesGroupSchema])
def list_recipes_groups(request):
    groups = RecipesGroup.objects.all()
    return [RecipesGroupSchema.from_orm(group) for group in groups]


@router.get("/recipes-groups/{group_id}", response=RecipesGroupSchema)
def get_recipes_group(request, group_id: int):
    group = RecipesGroup.objects.get(id=group_id)
    return RecipesGroupSchema.from_orm(group)


@router.post("/recipes-groups", response=RecipesGroupSchema)
def create_recipes_group(request, payload: RecipesGroupSchema):
    group = RecipesGroup.objects.create(**payload.dict())
    return RecipesGroupSchema.from_orm(group)


@router.put("/recipes-groups/{group_id}", response=RecipesGroupSchema)
def update_recipes_group(request, group_id: int, payload: RecipesGroupSchema):
    group = RecipesGroup.objects.get(id=group_id)
    for attr, value in payload.dict().items():
        setattr(group, attr, value)
    group.save()
    return RecipesGroupSchema.from_orm(group)


@router.delete("/recipes-groups/{group_id}")
def delete_recipes_group(request, group_id: int):
    group = RecipesGroup.objects.get(id=group_id)
    group.delete()
    return {"success": True}


@router.get("/recipes", response=List[RecipesSchema])
def list_recipes(request):
    recipes = Recipes.objects.all()
    return [RecipesSchema.from_orm(recipe) for recipe in recipes]


@router.get("/recipes/{recipe_id}", response=RecipesSchema)
def get_recipe(request, recipe_id: int):
    recipe = Recipes.objects.get(id=recipe_id)
    return RecipesSchema.from_orm(recipe)


"""
@router.post("/recipes", response=RecipesSchema)
def create_recipe(request, payload: RecipesSchema):
    # Create the recipe
    recipe_data = payload.dict(exclude={'goods'})
    recipe = Recipes.objects.create(**recipe_data)

    # Create the related RecipeGoods if goods are provided
    if payload.goods:
        for item in payload.goods:
            RecipeGoods.objects.create(
                recipe=recipe,
                goods=Goods.objects.get(id=item.goods_id),
                count=item.count
            )

    return RecipesSchema.from_orm(recipe)
"""


@router.post("/recipes", response=RecipesSchema)
def create_recipe(request, payload: RecipeCreateSchema):
    # Fetch the RecipesGroup instance
    group = RecipesGroup.objects.get(id=payload.group)

    # Create the recipe
    recipe = Recipes.objects.create(
        name=payload.name,
        icon=payload.icon,
        description=payload.description,
        group=group,
        is_local=payload.is_local,
        cooking_time_max=payload.cooking_time_max,
        cooking_time_min=payload.cooking_time_min
    )

    # Create the related RecipeGoods if goods are provided
    if payload.goods:
        for item in payload.goods:
            RecipeGoods.objects.create(
                recipe=recipe,
                goods_id=item.goods_id,
                count=item.count
            )

    return RecipesSchema.from_orm(recipe)


"""
@router.put("/recipes/{recipe_id}", response=RecipesSchema)
def update_recipe(request, recipe_id: int, payload: RecipesSchema):
    recipe = Recipes.objects.get(id=recipe_id)
    for attr, value in payload.dict().items():
        setattr(recipe, attr, value)
    recipe.save()
    return RecipesSchema.from_orm(recipe)

@router.delete("/recipes/{recipe_id}")
def delete_recipe(request, recipe_id: int):
    recipe = Recipes.objects.get(id=recipe_id)
    recipe.delete()
    return {"success": True}
"""


@router.put("/recipes/{recipe_id}", response=RecipesSchema)
def update_recipe(request, recipe_id: int, payload: RecipeUpdateSchema):
    recipe = Recipes.objects.get(id=recipe_id)

    for attr, value in payload.dict(exclude_unset=True).items():
        if attr == 'group' and value is not None:
            value = RecipesGroup.objects.get(id=value)
        elif attr == 'goods' and value is not None:
            RecipeGoods.objects.filter(recipe=recipe).delete()
            for item in value:
                RecipeGoods.objects.create(
                    recipe=recipe,
                    goods_id=item['goods_id'],
                    count=item['count']
                )
            continue
        setattr(recipe, attr, value)

    recipe.save()
    return RecipesSchema.from_orm(recipe)


@router.post("/recipes/batch", response=List[RecipesSchema])
def create_recipes_batch(request, payload: RecipesBatchCreateSchema):
    recipes = []
    for recipe_data in payload.recipes:
        group = RecipesGroup.objects.get(id=recipe_data.group)
        recipe = Recipes.objects.create(
            name=recipe_data.name,
            icon=recipe_data.icon,
            description=recipe_data.description,
            group=group,
            is_local=recipe_data.is_local,
            cooking_time_max=recipe_data.cooking_time_max,
            cooking_time_min=recipe_data.cooking_time_min
        )
        recipes.append(RecipesSchema.from_orm(recipe))
    return recipes


@router.put("/recipes/batch", response=List[RecipesSchema])
def update_recipes_batch(request, payload: RecipesBatchUpdateSchema):
    recipes = []
    for recipe_data in payload.recipes:
        recipe = Recipes.objects.get(id=recipe_data.id)
        for attr, value in recipe_data.dict(exclude_unset=True).items():
            setattr(recipe, attr, value)
        recipe.save()
        recipes.append(RecipesSchema.from_orm(recipe))
    return recipes


@router.get("/families", response=List[FamiliesSchema])
def list_families(request):
    families = Families.objects.all()
    return [FamiliesSchema.from_orm(family) for family in families]


@router.get("/families/{family_id}", response=FamiliesSchema)
def get_family(request, family_id: int):
    family = Families.objects.get(id=family_id)
    return FamiliesSchema.from_orm(family)


@router.post("/families", response=FamiliesSchema)
def create_family(request, payload: FamiliesSchema):
    family = Families.objects.create(**payload.dict())
    return FamiliesSchema.from_orm(family)


@router.put("/families/{family_id}", response=FamiliesSchema)
def update_family(request, family_id: int, payload: FamiliesSchema):
    family = Families.objects.get(id=family_id)
    for attr, value in payload.dict().items():
        setattr(family, attr, value)
    family.save()
    return FamiliesSchema.from_orm(family)


@router.delete("/families/{family_id}")
def delete_family(request, family_id: int):
    family = Families.objects.get(id=family_id)
    family.delete()
    return {"success": True}


@router.get("/family-members", response=List[FamilyMembersSchema])
def list_family_members(request):
    members = FamilyMembers.objects.all()
    return [FamilyMembersSchema.from_orm(member) for member in members]


@router.get("/family-members/{member_id}", response=FamilyMembersSchema)
def get_family_member(request, member_id: int):
    member = FamilyMembers.objects.get(id=member_id)
    return FamilyMembersSchema.from_orm(member)


@router.post("/family-members", response=FamilyMembersSchema)
def create_family_member(request, payload: FamilyMembersSchema):
    member = FamilyMembers.objects.create(**payload.dict())
    return FamilyMembersSchema.from_orm(member)


@router.put("/family-members/{member_id}", response=FamilyMembersSchema)
def update_family_member(request, member_id: int, payload: FamilyMembersSchema):
    member = FamilyMembers.objects.get(id=member_id)
    for attr, value in payload.dict().items():
        setattr(member, attr, value)
    member.save()
    return FamilyMembersSchema.from_orm(member)


@router.delete("/family-members/{member_id}")
def delete_family_member(request, member_id: int):
    member = FamilyMembers.objects.get(id=member_id)
    member.delete()
    return {"success": True}


@router.get("/family-recipes", response=List[FamilyRecipesSchema])
def list_family_recipes(request):
    family_recipes = FamilyRecipes.objects.all()
    return [FamilyRecipesSchema.from_orm(family_recipe) for family_recipe in family_recipes]


@router.get("/family-recipes/{family_recipe_id}", response=FamilyRecipesSchema)
def get_family_recipe(request, family_recipe_id: int):
    family_recipe = FamilyRecipes.objects.get(id=family_recipe_id)
    return FamilyRecipesSchema.from_orm(family_recipe)


@router.post("/family-recipes", response=FamilyRecipesSchema)
def create_family_recipe(request, payload: FamilyRecipesSchema):
    family_recipe = FamilyRecipes.objects.create
    return FamilyRecipesSchema.from_orm(family_recipe)


@router.put("/family-recipes/{family_recipe_id}", response=FamilyRecipesSchema)
def update_family_recipe(request, family_recipe_id: int, payload: FamilyRecipesSchema):
    family_recipe = FamilyRecipes.objects.get(id=family_recipe_id)
    for attr, value in payload.dict().items():
        setattr(family_recipe, attr, value)
    family_recipe.save()
    return FamilyRecipesSchema.from_orm(family_recipe)


@router.delete("/family-recipes/{family_recipe_id}")
def delete_family_recipe(request, family_recipe_id: int):
    family_recipe = FamilyRecipes.objects.get(id=family_recipe_id)
    family_recipe.delete()
    return {"success": True}


@router.get("/family-goods-in-stock", response=List[FamilyGoodsInStockSchema])
def list_family_goods_in_stock(request):
    family_goods_in_stock = FamilyGoodsInStock.objects.all()
    return [FamilyGoodsInStockSchema.from_orm(stock) for stock in family_goods_in_stock]


@router.get("/family-goods-in-stock/{stock_id}", response=FamilyGoodsInStockSchema)
def get_family_good_in_stock(request, stock_id: int):
    stock = FamilyGoodsInStock.objects.get(id=stock_id)
    return FamilyGoodsInStockSchema.from_orm(stock)


@router.post("/family-goods-in-stock", response=FamilyGoodsInStockSchema)
def create_family_good_in_stock(request, payload: FamilyGoodsInStockSchema):
    stock = FamilyGoodsInStock.objects.create(**payload.dict())
    return FamilyGoodsInStockSchema.from_orm(stock)


@router.put("/family-goods-in-stock/{stock_id}", response=FamilyGoodsInStockSchema)
def update_family_good_in_stock(request, stock_id: int, payload: FamilyGoodsInStockSchema):
    stock = FamilyGoodsInStock.objects.get(id=stock_id)
    for attr, value in payload.dict().items():
        setattr(stock, attr, value)
    stock.save()
    return FamilyGoodsInStockSchema.from_orm(stock)


@router.delete("/family-goods-in-stock/{stock_id}")
def delete_family_good_in_stock(request, stock_id: int):
    stock = FamilyGoodsInStock.objects.get(id=stock_id)
    stock.delete()
    return {"success": True}
