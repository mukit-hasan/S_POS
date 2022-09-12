# Generated by Django 4.1 on 2022-08-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]