# Generated by Django 4.0.6 on 2022-07-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0017_profile_interest_profile_interest2_profile_interest3'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(default='Unemployed', max_length=255),
        ),
    ]