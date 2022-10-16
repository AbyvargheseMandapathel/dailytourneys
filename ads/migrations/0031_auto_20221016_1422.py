# Generated by Django 3.2.13 on 2022-10-16 14:22

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('ads', '0030_remove_ads_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='brand',
            new_name='no_of_slots',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='price',
            new_name='prize',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='state',
        ),
        migrations.RemoveField(
            model_name='adsimages',
            name='image',
        ),
        migrations.AddField(
            model_name='ads',
            name='entry',
            field=models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='img_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='registeration_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]