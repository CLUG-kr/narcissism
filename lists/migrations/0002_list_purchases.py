# Generated by Django 2.2.5 on 2021-02-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchases', '0001_initial'),
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='purchases',
            field=models.ManyToManyField(blank=True, to='purchases.Purchase'),
        ),
    ]
