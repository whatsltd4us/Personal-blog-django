# Generated by Django 3.0.4 on 2020-05-05 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.TextField(blank=True, max_length=155),
        ),
    ]
