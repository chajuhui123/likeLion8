# Generated by Django 3.0.6 on 2020-05-23 03:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('youtuberApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='youtuber',
            name='summary',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
