# Generated by Django 2.2.5 on 2021-02-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/media/404_not_found.png', null=True, upload_to='', verbose_name='サムネイル'),
        ),
    ]
