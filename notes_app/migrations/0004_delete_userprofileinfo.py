# Generated by Django 3.0.3 on 2020-03-31 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0003_userprofileinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
