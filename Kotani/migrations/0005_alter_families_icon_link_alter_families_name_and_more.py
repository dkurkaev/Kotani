# Generated by Django 4.2.13 on 2024-05-28 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Kotani', '0004_alter_goods_icon_link_alter_goods_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='families',
            name='icon_link',
            field=models.CharField(max_length=255, null=True, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='families',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='familygoodsinstock',
            name='change_date',
            field=models.DateTimeField(verbose_name='Изменено'),
        ),
        migrations.AlterField(
            model_name='familygoodsinstock',
            name='change_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Изменил'),
        ),
        migrations.AlterField(
            model_name='familygoodsinstock',
            name='count',
            field=models.FloatField(verbose_name='Количество в наличии'),
        ),
        migrations.AlterField(
            model_name='familygoodsinstock',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.families', verbose_name='Семья'),
        ),
        migrations.AlterField(
            model_name='familygoodsinstock',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.goods', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='familymembers',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.families', verbose_name='Семья'),
        ),
        migrations.AlterField(
            model_name='familymembers',
            name='is_chef',
            field=models.BooleanField(verbose_name='Шеф'),
        ),
        migrations.AlterField(
            model_name='familymembers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='familyrecipes',
            name='add_date',
            field=models.DateTimeField(null=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='familyrecipes',
            name='chef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Шеф рецепта'),
        ),
        migrations.AlterField(
            model_name='familyrecipes',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.families', verbose_name='Семья'),
        ),
        migrations.AlterField(
            model_name='familyrecipes',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='familyrecipes',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.recipes', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='icon_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='is_local',
            field=models.BooleanField(verbose_name='Локальный'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.measure', verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(default='Продукт', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Kotani.goods', verbose_name='Вышестоящий продукт'),
        ),
        migrations.AlterField(
            model_name='measure',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='change_datetime',
            field=models.DateTimeField(verbose_name='Изменено'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='change_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Изменил'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='comment',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.orders', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='order_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.orderstatus', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='change_datetime',
            field=models.DateTimeField(verbose_name='Изменено'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='change_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_change_user', to=settings.AUTH_USER_MODEL, verbose_name='Изменил'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='comment',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_customer', to=settings.AUTH_USER_MODEL, verbose_name='Заказал'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.families', verbose_name='Семья'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.recipes', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.orderstatus', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recipegoods',
            name='count',
            field=models.FloatField(null=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipegoods',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.goods', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='recipegoods',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.recipes', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='cooking_time_max',
            field=models.IntegerField(verbose_name='Время приготовления, до (мин)'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='cooking_time_min',
            field=models.IntegerField(null=True, verbose_name='Время приготовления, от (мин)'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.recipesgroup', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='icon_link',
            field=models.CharField(max_length=255, null=True, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='is_local',
            field=models.BooleanField(verbose_name='Локальный'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='recipesgroup',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.families', verbose_name='Семья'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kotani.recipes', verbose_name='Рецепт'),
        ),
    ]
