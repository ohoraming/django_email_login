# Generated by Django 4.0.4 on 2022-05-26 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='account_id',
            new_name='user_id',
        ),
    ]