# Generated by Django 3.0.6 on 2020-05-30 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_selectedlist_employer_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='zip',
            new_name='zip_code',
        ),
    ]
