# Generated by Django 3.1.1 on 2020-10-09 20:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0014_custompage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custompage',
            name='Name',
        ),
        migrations.AddField(
            model_name='custompage',
            name='linkName',
            field=models.CharField(default='rules', max_length=200, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='custompage',
            name='only_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='custompage',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='custompage',
            name='title',
            field=models.CharField(default='default', max_length=1000),
            preserve_default=False,
        ),
    ]
