# Generated by Django 3.0.7 on 2021-04-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_cuspack_no_of_cars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuspack',
            name='package',
        ),
        migrations.AddField(
            model_name='cuspack',
            name='total_cars',
            field=models.IntegerField(default=1),
        ),
    ]
