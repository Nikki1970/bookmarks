# Generated by Django 3.1.7 on 2021-04-26 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarksapp', '0004_auto_20210424_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folder',
            old_name='name',
            new_name='f_name',
        ),
    ]
