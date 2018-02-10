# Generated by Django 2.0.1 on 2018-02-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20180202_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.FileField(upload_to='teacher/image'),
        ),
    ]