# Generated by Django 4.0.6 on 2022-07-18 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='super',
            name='catchphrase',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype'),
            preserve_default=False,
        ),
    ]
