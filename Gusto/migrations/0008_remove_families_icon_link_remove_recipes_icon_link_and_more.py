# Generated by Django 4.2.13 on 2024-05-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gusto', '0007_remove_goods_icon_link_goods_icon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='families',
            name='icon_link',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='icon_link',
        ),
        migrations.AddField(
            model_name='families',
            name='icon',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='icon',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
