# Generated by Django 5.0.7 on 2024-08-12 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_streamingplatforms_watchlist_delete_movie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StreamingPlatforms',
            new_name='StreamingPlatform',
        ),
    ]
