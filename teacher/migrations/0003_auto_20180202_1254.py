# Generated by Django 2.0.1 on 2018-02-02 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20180202_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
