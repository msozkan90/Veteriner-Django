# Generated by Django 3.2.7 on 2022-02-14 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hayvan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('genus', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='HayvanSahibi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=11)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hayvanlar.hayvan')),
            ],
        ),
    ]