# Generated by Django 4.0 on 2021-12-21 14:42

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='holiday',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='name cannot be less than 2 char')])),
                ('type', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='type cannot be less than 2 char')])),
                ('startDate', models.DateField()),
                ('noOfDays', models.PositiveIntegerField()),
                ('endDate', models.DateField()),
            ],
        ),
    ]