# Generated by Django 4.2.1 on 2023-09-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0029_delete_hotels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_addresss', models.TextField()),
                ('hotel_rating', models.IntegerField()),
                ('hotel_price', models.IntegerField()),
                ('hotel_location', models.CharField(max_length=50)),
                ('hotel_Mainimage', models.ImageField(upload_to='hotels')),
                ('hotel_image1', models.ImageField(upload_to='hotels')),
                ('hotel_image2', models.ImageField(upload_to='hotels')),
                ('hotel_image3', models.ImageField(upload_to='hotels')),
            ],
        ),
    ]
