# Generated by Django 3.2.7 on 2022-02-15 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hayvanlar', '0005_auto_20220215_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hayvan',
            name='owner',
        ),
        migrations.AddField(
            model_name='hayvansahibi',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hayvanlar.hayvan'),
        ),
    ]