# Generated by Django 3.0.6 on 2020-06-16 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20200616_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='labour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.LaboursProfile'),
        ),
    ]