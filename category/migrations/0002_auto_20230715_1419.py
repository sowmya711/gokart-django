# Generated by Django 3.1 on 2023-07-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.SlugField(unique=True),
        ),
    ]
