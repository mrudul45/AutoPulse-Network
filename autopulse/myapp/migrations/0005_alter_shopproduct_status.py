# Generated by Django 4.2.7 on 2023-11-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_shopproduct_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
