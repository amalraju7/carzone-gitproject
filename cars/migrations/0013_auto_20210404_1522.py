# Generated by Django 3.0.7 on 2021-04-04 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_auto_20210404_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='created_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]