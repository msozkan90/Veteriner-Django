# Generated by Django 3.2.7 on 2022-02-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hayvanlar', '0003_hayvan_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hayvan',
            name='age',
            field=models.IntegerField(default=0, max_length=200),
        ),
    ]
