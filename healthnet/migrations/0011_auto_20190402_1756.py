# Generated by Django 2.0.9 on 2019-04-02 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthnet', '0010_auto_20190330_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='sex',
            new_name='gender',
        ),
        migrations.AddField(
            model_name='patient',
            name='familyHistory',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='medicalHistory',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='admission',
            name='date',
            field=models.DateField(default=datetime.date(2019, 4, 2)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthday',
            field=models.DateField(default=datetime.date(2002, 1, 1)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
