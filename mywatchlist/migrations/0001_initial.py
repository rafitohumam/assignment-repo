# Generated by Django 4.1 on 2022-09-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField()),
                ('description', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('release_date', models.TimeField()),
                ('review', models.TextField()),
            ],
        ),
    ]