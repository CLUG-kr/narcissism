# Generated by Django 2.2.5 on 2021-02-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210131_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='kakao_id',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]