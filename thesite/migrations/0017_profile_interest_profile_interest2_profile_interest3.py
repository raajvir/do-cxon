# Generated by Django 4.0.6 on 2022-07-18 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0016_post_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.CharField(default='Uncategorized', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest2',
            field=models.CharField(default='Uncategorized', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest3',
            field=models.CharField(default='Uncategorized', max_length=255),
        ),
    ]
