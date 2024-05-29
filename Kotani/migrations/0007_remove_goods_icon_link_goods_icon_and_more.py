# Generated by Django 4.2.13 on 2024-05-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kotani', '0006_alter_families_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='icon_link',
        ),
        migrations.AddField(
            model_name='goods',
            name='icon',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterUniqueTogether(
            name='recipegoods',
            unique_together={('recipe', 'goods')},
        ),
    ]