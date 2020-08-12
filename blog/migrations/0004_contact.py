# Generated by Django 3.0.8 on 2020-08-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('rad', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
