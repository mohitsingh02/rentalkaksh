# Generated by Django 3.0.8 on 2020-08-06 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='UName',
        ),
    ]
