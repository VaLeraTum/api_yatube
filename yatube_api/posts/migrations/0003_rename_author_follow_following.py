# Generated by Django 3.2.16 on 2023-04-06 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230405_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]
