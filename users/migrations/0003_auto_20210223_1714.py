# Generated by Django 2.2.5 on 2021-02-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_email_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_code',
            field=models.CharField(blank=True, default='', max_length=6),
        ),
    ]