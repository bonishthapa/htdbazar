# Generated by Django 3.0.3 on 2020-06-26 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_order_orderprouct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderProuct',
            new_name='OrderProduct',
        ),
    ]
