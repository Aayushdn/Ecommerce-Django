# Generated by Django 3.1 on 2020-09-04 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_remove_orderupdate_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]
