# Generated by Django 3.0.8 on 2020-08-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200812_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='owner_phone',
            field=models.BigIntegerField(),
        ),
    ]