# Generated by Django 4.1.1 on 2022-10-28 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortener',
            old_name='url_long',
            new_name='long_url',
        ),
        migrations.RenameField(
            model_name='shortener',
            old_name='url_short',
            new_name='short_url',
        ),
    ]
