# Generated by Django 4.2.5 on 2023-11-29 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0041_package_feedback_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_place', models.CharField(max_length=50)),
                ('b_desc', models.TextField()),
                ('b_img', models.CharField(max_length=150)),
                ('blogger', models.CharField(max_length=50)),
            ],
        ),
    ]
