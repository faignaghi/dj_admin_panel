# Generated by Django 4.1.2 on 2022-10-18 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_alter_product_options_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, default='defaults/clarusway.png', null=True, upload_to='product/'),
        ),
    ]