# Generated by Django 4.2.7 on 2023-11-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_shopproduct_shopkeeper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('not_available', 'Not Available')], default='available', max_length=15),
        ),
    ]
