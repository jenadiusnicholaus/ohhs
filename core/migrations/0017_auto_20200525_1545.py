# Generated by Django 3.0.6 on 2020-05-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200525_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='labour',
        ),
        migrations.AddField(
            model_name='laboursprofile',
            name='comments',
            field=models.ManyToManyField(to='core.comments'),
        ),
    ]
