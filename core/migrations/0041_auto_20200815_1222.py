# Generated by Django 3.0.7 on 2020-08-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_labourofficialdoc_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboursprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='laboursprofile',
            name='Full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
