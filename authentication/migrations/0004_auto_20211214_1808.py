# Generated by Django 3.2.8 on 2021-12-14 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='national_id',
            new_name='nationalID',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='phoneNumber',
        ),
    ]