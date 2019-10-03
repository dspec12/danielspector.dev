# Generated by Django 2.2.6 on 2019-10-03 21:12

import autoslug.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20191002_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='temp', editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 3, 21, 12, 23, 704773)),
        ),
    ]