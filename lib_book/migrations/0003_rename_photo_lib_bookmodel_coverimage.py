# Generated by Django 3.2.6 on 2021-10-23 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib_book', '0002_auto_20211023_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lib_bookmodel',
            old_name='photo',
            new_name='coverImage',
        ),
    ]
