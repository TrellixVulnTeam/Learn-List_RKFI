# Generated by Django 2.0.4 on 2018-05-27 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_playlist_picture_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='picture_link',
            new_name='picture',
        ),
    ]
