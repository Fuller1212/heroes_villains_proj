# Generated by Django 4.0.6 on 2022-07-18 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_super_catchphrase_super_super_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='second_ability',
            new_name='secondary_ability',
        ),
    ]