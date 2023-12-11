# Generated by Django 3.0.7 on 2023-12-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=50)),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
