# Generated by Django 2.2.9 on 2020-03-16 06:06

from django.db import migrations, models
import mysite.utils


class Migration(migrations.Migration):

    dependencies = [
        ('thumb_page', '0004_auto_20200316_0604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=mysite.utils.uuid_upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]