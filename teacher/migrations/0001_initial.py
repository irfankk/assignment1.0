# Generated by Django 2.0.1 on 2018-02-02 12:38

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('teacher', models.BooleanField(default=False)),
                ('phone_number', models.CharField(default='9895098950', max_length=12, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(default='Bangalore', max_length=300)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.FileField(default='teacher/index.jpeg', upload_to='teacher/%Y/%m/%d')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
