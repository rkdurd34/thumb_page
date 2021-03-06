# Generated by Django 2.2.9 on 2020-03-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumb_page', '0003_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='desc',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
