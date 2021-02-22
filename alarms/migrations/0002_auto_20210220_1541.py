# Generated by Django 2.2.5 on 2021-02-20 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alarms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alarm_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alarm',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alarm_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]