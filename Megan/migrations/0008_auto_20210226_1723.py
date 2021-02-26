# Generated by Django 3.1.5 on 2021-02-26 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Megan', '0007_auto_20210226_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessages',
            old_name='_id',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='usermessages',
            name='text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
