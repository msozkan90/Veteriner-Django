# Generated by Django 3.2.7 on 2022-02-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hayvanlar', '0007_auto_20220215_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hayvansahibi',
            name='address',
            field=models.TextField(max_length=200),
        ),
    ]