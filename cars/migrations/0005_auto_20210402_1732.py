# Generated by Django 3.0.7 on 2021-04-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_brand_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
