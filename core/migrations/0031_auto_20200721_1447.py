# Generated by Django 3.0.7 on 2020-07-21 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_selectedlist_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectedlist',
            name='amount',
        ),
        migrations.AddField(
            model_name='selectedlist',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Payment'),
        ),
    ]