# Generated by Django 3.0.8 on 2020-08-09 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200809_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='img1',
            field=models.ImageField(default='default_room.jpg', upload_to='room_pics'),
        ),
        migrations.AlterField(
            model_name='room',
            name='img2',
            field=models.ImageField(default='default_room.jpg', upload_to='room_pics'),
        ),
        migrations.AlterField(
            model_name='room',
            name='img3',
            field=models.ImageField(default='default_room.jpg', upload_to='room_pics'),
        ),
    ]