# Generated by Django 3.2.7 on 2022-02-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hayvanlar', '0002_auto_20220215_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='hayvan',
            name='age',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
