# Generated by Django 3.2.13 on 2023-11-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('range', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Range',
        ),
    ]
