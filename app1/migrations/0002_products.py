# Generated by Django 3.0.7 on 2023-12-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image', models.CharField(max_length=2500)),
            ],
        ),
    ]
