# Generated by Django 2.0.1 on 2018-02-02 12:38

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.FileField(default='student/index.jpeg', upload_to='student/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='student',
            name='location',
            field=models.CharField(default='Bangalore', max_length=300),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='9895098950', max_length=12, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
