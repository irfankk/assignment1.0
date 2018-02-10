# Generated by Django 2.0.1 on 2018-02-03 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20180202_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='resume',
            field=models.FileField(default=django.utils.timezone.now, upload_to='student/resuem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(upload_to='student/image'),
        ),
    ]
