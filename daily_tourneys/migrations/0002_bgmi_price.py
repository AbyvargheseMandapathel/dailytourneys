# Generated by Django 3.2.13 on 2022-07-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_tourneys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bgmi',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
