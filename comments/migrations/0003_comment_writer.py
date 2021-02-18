# Generated by Django 2.2.5 on 2021-02-18 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0002_comment_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]