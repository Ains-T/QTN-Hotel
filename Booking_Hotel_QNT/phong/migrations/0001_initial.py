# Generated by Django 2.2.6 on 2019-12-18 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phong',
            fields=[
                ('sophong', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tenloaiphong', models.CharField(max_length=50)),
                ('gia', models.BigIntegerField(max_length=50)),
            ],
        ),
    ]
