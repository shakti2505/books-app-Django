# Generated by Django 4.1.4 on 2022-12-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('book_desc', models.CharField(max_length=200)),
                ('book_price', models.IntegerField()),
                ('book_rating', models.FloatField()),
            ],
        ),
    ]
