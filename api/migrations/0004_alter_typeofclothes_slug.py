# Generated by Django 4.1.4 on 2022-12-15 15:14

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_typeofclothes_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeofclothes',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='type_name'),
        ),
    ]
