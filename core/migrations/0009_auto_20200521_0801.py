# Generated by Django 3.0.6 on 2020-05-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200521_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='laboursprofile',
            name='image',
            field=models.FileField(null=True, upload_to='profile_pic'),
        ),
    ]