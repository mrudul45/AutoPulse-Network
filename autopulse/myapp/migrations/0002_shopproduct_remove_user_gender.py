# Generated by Django 4.2.7 on 2023-11-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_specification', models.TextField()),
                ('manufacture_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]
