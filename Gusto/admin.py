from django.contrib import admin
from .models import (
    Measure,
    Goods,
    RecipesGroup,
    Recipes,
    RecipeGoods,
    Schedule,
    OrderStatus,
    Orders,
    OrderHistory,
    Families,
    FamilyMembers,
    FamilyRecipes,
    FamilyGoodsInStock
)


"""
@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon_link', 'measure', 'is_local', 'owner', 'parent']
    search_fields = ['name', 'icon_link']
    list_filter = ['is_local']

@admin.register(RecipesGroup)
class RecipesGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon_link', 'description', 'group', 'is_local', 'owner', 'cooking_time_min', 'cooking_time_max']
    search_fields = ['name', 'description']
    list_filter = ['is_local']

@admin.register(RecipeGoods)
class RecipeGoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'goods', 'count']
    search_fields = ['recipe__name', 'goods__name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'date', 'family']
    search_fields = ['recipe__name', 'family__name']
    list_filter = ['date']


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'date', 'family', 'customer', 'status', 'change_datetime', 'change_user', 'comment']
    search_fields = ['recipe__name', 'customer__name', 'comment']
    list_filter = ['date', 'status', 'change_datetime']

@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'order_status', 'change_datetime', 'change_user', 'comment']
    search_fields = ['order__id', 'order_status__name', 'comment']
    list_filter = ['change_datetime']

@admin.register(Families)
class FamiliesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon_link']
    search_fields = ['name']

@admin.register(FamilyMembers)
class FamilyMembersAdmin(admin.ModelAdmin):
    list_display = ['family', 'user', 'is_chef']
    search_fields = ['family__name', 'user__name']
    list_filter = ['is_chef']

@admin.register(FamilyRecipes)
class FamilyRecipesAdmin(admin.ModelAdmin):
    list_display = ['id', 'family', 'recipe', 'add_date', 'is_active', 'chef']
    search_fields = ['family__name', 'recipe__name']
    list_filter = ['add_date', 'is_active']

@admin.register(FamilyGoodsInStock)
class FamilyGoodsInStockAdmin(admin.ModelAdmin):
    list_display = ['id', 'family', 'goods', 'count', 'change_date', 'change_user']
    search_fields = ['family__name', 'goods__name']
    list_filter = ['change_date']

"""

# Register all models to the admin site
# Alternatively, you can use admin.site.register(ModelName) for a simpler registration without customization

admin.site.register(Measure)
admin.site.register(Goods)
admin.site.register(RecipesGroup)
admin.site.register(Recipes)
admin.site.register(RecipeGoods)
admin.site.register(Schedule)
admin.site.register(OrderStatus)
admin.site.register(Orders)
admin.site.register(OrderHistory)
admin.site.register(Families)
admin.site.register(FamilyMembers)
admin.site.register(FamilyRecipes)
admin.site.register(FamilyGoodsInStock)

