# Generated by Django 4.2.5 on 2023-10-04 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='Category',
            new_name='category',
        ),
    ]
