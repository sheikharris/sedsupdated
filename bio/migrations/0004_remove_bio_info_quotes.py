# Generated by Django 3.0.3 on 2020-04-13 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0003_bio_info_quotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio_info',
            name='quotes',
        ),
    ]