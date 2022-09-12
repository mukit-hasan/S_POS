# Generated by Django 4.1 on 2022-08-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('descriptions', models.TextField(blank=True, max_length=1000, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('category', models.CharField(choices=[('Burger', 'Burger'), ('Fried Chicken', 'Fried Chicken'), ('Beverage', 'Beverage'), ('Dessert', 'Dessert')], max_length=200, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
