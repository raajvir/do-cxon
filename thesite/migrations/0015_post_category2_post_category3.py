# Generated by Django 4.0.5 on 2022-07-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0014_profile_facebook_url_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category2',
            field=models.CharField(default='Uncategorized', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='category3',
            field=models.CharField(default='Uncategorized', max_length=255),
        ),
    ]