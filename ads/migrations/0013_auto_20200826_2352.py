# Generated by Django 2.2.15 on 2020-08-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0012_auto_20200826_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='category',
        ),
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.ManyToManyField(to='ads.Category'),
        ),
    ]