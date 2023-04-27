# Generated by Django 4.2 on 2023-04-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quickstart", "0003_wishlist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wishlist",
            name="product",
        ),
        migrations.AddField(
            model_name="wishlist",
            name="product",
            field=models.ManyToManyField(
                related_name="wishlists", to="quickstart.product"
            ),
        ),
    ]
