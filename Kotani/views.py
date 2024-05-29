from rest_framework import viewsets, generics
from .models import Measure, Goods, RecipesGroup, Recipes, RecipeGoods, Schedule, OrderStatus, Orders, OrderHistory, \
    Families, FamilyMembers, FamilyRecipes, FamilyGoodsInStock



class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

#    def get_serializer_context(self):
#        # Pass the request context to the serializer
#        context = super().get_serializer_context()
#        context['request'] = self.request
#        return context

    def get_serializer_context(self):
        # Pass the request context to the serializer
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class RecipesGroupViewSet(viewsets.ModelViewSet):
    queryset = RecipesGroup.objects.all()
    serializer_class = RecipesGroupSerializer


#class RecipesViewSet(viewsets.ModelViewSet):
#    queryset = Recipes.objects.all()
#    serializer_class = RecipesSerializer

class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer


class RecipeGoodsViewSet(viewsets.ModelViewSet):
    queryset = RecipeGoods.objects.all()
    serializer_class = RecipeGoodsSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderHistoryViewSet(viewsets.ModelViewSet):
    queryset = OrderHistory.objects.all()
    serializer_class = OrderHistorySerializer


class FamiliesViewSet(viewsets.ModelViewSet):
    queryset = Families.objects.all()
    serializer_class = FamiliesSerializer


class FamilyMembersViewSet(viewsets.ModelViewSet):
    queryset = FamilyMembers.objects.all()
    serializer_class = FamilyMembersSerializer


class FamilyRecipesViewSet(viewsets.ModelViewSet):
    queryset = FamilyRecipes.objects.all()
    serializer_class = FamilyRecipesSerializer


class FamilyGoodsInStockViewSet(viewsets.ModelViewSet):
    queryset = FamilyGoodsInStock.objects.all()
    serializer_class = FamilyGoodsInStockSerializer
