from django.db import models
from django.contrib.auth.models import User  # Import the default User model


class Measure(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"


class Goods(models.Model):
    def __str__(self):
        return self.name

    parent = models.ForeignKey('self', verbose_name="Вышестоящий продукт", on_delete=models.CASCADE, null=True,
                               blank=True)
    name = models.CharField(verbose_name="Название", max_length=255, default="Продукт")
    icon = models.ImageField(upload_to='images/', null=True, blank=True)
    measure = models.ForeignKey(Measure, verbose_name="Единица измерения", on_delete=models.CASCADE, default=1)
    is_local = models.BooleanField(verbose_name="Локальный",default=False)
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, null=True,
                              blank=True)  # Updated reference

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class RecipesGroup(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Группа рецептов"
        verbose_name_plural = "Группы рецептов"


class Recipes(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField("Название", max_length=255)
    icon = models.ImageField(upload_to='images/', null=True)
    description = models.TextField("Описание")
    group = models.ForeignKey(RecipesGroup, verbose_name="Группа", on_delete=models.CASCADE)
    is_local = models.BooleanField("Локальный")
    #goods = models.ManyToManyField(Goods, related_name='recipes')
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, null=True)  # Updated reference
    cooking_time_min = models.IntegerField("Время приготовления, от (мин)", null=True)
    cooking_time_max = models.IntegerField("Время приготовления, до (мин)")

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class RecipeGoods(models.Model):
    def __str__(self):
        return f"{self.recipe} | {self.goods} | {self.count}"

    recipe = models.ForeignKey(Recipes, related_name='recipe_goods', verbose_name="Рецепт", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="Продукт", on_delete=models.CASCADE)
    count = models.FloatField("Количество", null=True)

    class Meta:
        def __str__(self):
            return self.name
        unique_together = ('recipe', 'goods')

        verbose_name = "Продукт для рецепта"
        verbose_name_plural = "Продукты для рецептов"


class Schedule(models.Model):
    def __str__(self):
        return self.name

    recipe = models.ForeignKey(Recipes, verbose_name="Рецепт", on_delete=models.CASCADE)
    date = models.DateField("Дата")
    family = models.ForeignKey('Families', verbose_name="Семья", on_delete=models.CASCADE)

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"


class OrderStatus(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField("Название", max_length=255)

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"


class Orders(models.Model):
    def __str__(self):
        return self.name

    recipe = models.ForeignKey(Recipes, verbose_name="Рецепт", on_delete=models.CASCADE)
    date = models.DateField("Дата")
    family = models.ForeignKey('Families', verbose_name="Семья", on_delete=models.CASCADE)
    customer = models.ForeignKey(User, verbose_name="Заказал", on_delete=models.CASCADE,
                                 related_name='orders_customer')  # Updated reference
    status = models.ForeignKey(OrderStatus, verbose_name="Статус", on_delete=models.CASCADE)
    change_datetime = models.DateTimeField("Изменено")
    change_user = models.ForeignKey(User, verbose_name="Изменил", on_delete=models.CASCADE,
                                    related_name='orders_change_user')  # Updated reference
    comment = models.TextField("Комментарий", null=True)

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderHistory(models.Model):
    def __str__(self):
        return self.name

    order = models.ForeignKey(Orders, verbose_name="Заказ", on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, verbose_name="Статус", on_delete=models.CASCADE)
    change_datetime = models.DateTimeField(verbose_name="Изменено")
    change_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Изменил")  # Updated reference
    comment = models.TextField(verbose_name="Комментарий", null=True)

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "История заказов"
        verbose_name_plural = "История заказов"


class Families(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name="Имя", max_length=255)
    icon = models.ImageField(upload_to='images/', null=True)

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Семья"
        verbose_name_plural = "Семьи"


class FamilyMembers(models.Model):
    def __str__(self):
        return self.name

    family = models.ForeignKey(Families, verbose_name="Семья", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", )  # Updated reference
    is_chef = models.BooleanField(verbose_name="Шеф")

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Член семьи"
        verbose_name_plural = "Члены семьи"


class FamilyRecipes(models.Model):
    def __str__(self):
        return self.name

    family = models.ForeignKey(Families, on_delete=models.CASCADE, verbose_name="Семья")
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name="Рецепт")
    add_date = models.DateTimeField(null=True, verbose_name="Дата добавления")
    is_active = models.BooleanField(verbose_name="Активный", default=True)
    chef = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Шеф рецепта")  # Updated reference

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Рецепт семьи"
        verbose_name_plural = "Рецепты семьи"


class FamilyGoodsInStock(models.Model):
    def __str__(self):
        return self.name

    family = models.ForeignKey(Families, on_delete=models.CASCADE, verbose_name="Семья")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="Продукт")
    count = models.FloatField(verbose_name="Количество в наличии")
    change_date = models.DateTimeField(verbose_name="Изменено")
    change_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Изменил")  # Updated reference

    class Meta:
        def __str__(self):
            return self.name

        verbose_name = "Продукт в наличии в семье"
        verbose_name_plural = "Продукты в наличии в семье"
