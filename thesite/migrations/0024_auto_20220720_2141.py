# Generated by Django 3.2 on 2022-07-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0023_auto_20220720_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='position2',
            field=models.CharField(default='Uncategorized', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='position3',
            field=models.CharField(default='Uncategorized', max_length=255),
        ),
    ]