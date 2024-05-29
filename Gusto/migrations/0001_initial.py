# Generated by Django 4.2.13 on 2024-05-28 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Families',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon_link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon_link', models.CharField(max_length=255)),
                ('is_local', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon_link', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_local', models.BooleanField()),
                ('cooking_time_min', models.IntegerField()),
                ('cooking_time_max', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipesGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon_link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.families')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.recipes')),
            ],
        ),
        migrations.AddField(
            model_name='recipes',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.recipesgroup'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.users'),
        ),
        migrations.CreateModel(
            name='RecipeGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.goods')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.recipes')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('change_datetime', models.DateTimeField()),
                ('comment', models.TextField()),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_change_user', to='Gusto.users')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_customer', to='Gusto.users')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.families')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.recipes')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.orderstatus')),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_datetime', models.DateTimeField()),
                ('comment', models.TextField()),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.users')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.orders')),
                ('order_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.orderstatus')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.measure'),
        ),
        migrations.AddField(
            model_name='goods',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.users'),
        ),
        migrations.AddField(
            model_name='goods',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gusto.goods'),
        ),
        migrations.CreateModel(
            name='FamilyRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField()),
                ('is_active', models.BooleanField()),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.users')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.families')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.recipes')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_chef', models.BooleanField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.families')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.users')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyGoodsInStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField()),
                ('change_date', models.DateTimeField()),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.users')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.families')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gusto.goods')),
            ],
        ),
    ]