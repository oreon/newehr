# Generated by Django 2.0.9 on 2019-03-30 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthnet', '0009_auto_20190329_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='date',
            field=models.DateField(default=datetime.date(2019, 3, 30)),
        ),
    ]
