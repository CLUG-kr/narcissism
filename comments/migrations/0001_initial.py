# Generated by Django 2.2.5 on 2021-02-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('context', models.CharField(default=' ', max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
