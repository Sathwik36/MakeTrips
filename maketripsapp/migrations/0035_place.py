# Generated by Django 4.2.1 on 2023-09-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0034_delete_place_alter_travellerdetail_t_contactno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('placename', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('placedescription', models.TextField()),
                ('splace1', models.CharField(max_length=50)),
                ('splace1description', models.TextField()),
                ('splace2', models.CharField(max_length=50)),
                ('splace2description', models.TextField()),
                ('splace3', models.CharField(max_length=50)),
                ('splace3description', models.TextField()),
                ('splace4', models.CharField(max_length=50)),
                ('splace4description', models.TextField()),
                ('splace5', models.CharField(max_length=50)),
                ('splace5description', models.TextField()),
            ],
        ),
    ]
