# Generated by Django 2.2.9 on 2020-03-17 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thumb_page', '0005_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='king_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='king_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='king_class', to='thumb_page.king_class'),
        ),
    ]
