# Generated by Django 3.2 on 2022-07-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0022_discussion_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
