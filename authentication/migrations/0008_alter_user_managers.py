# Generated by Django 4.0 on 2021-12-14 22:02

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
