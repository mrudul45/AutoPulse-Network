# Generated by Django 4.2.7 on 2023-11-23 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_shopproduct_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='pp_image/'),
        ),
    ]
