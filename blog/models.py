from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100)
    Desc = models.CharField(max_length=300)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    post_img = models.ImageField(default='default.jpg', upload_to='post_pics')
    author = models.CharField(max_length=60)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Contact(models.Model):
    UName = models.CharField(max_length=100)
    Phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    rad = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.UName


class Room(models.Model):
    room = models.CharField(max_length=50)
    info = models.TextField()
    no_room = models.IntegerField()
    kitchen = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    adress = models.TextField()
    owner_name = models.CharField(max_length=100)
    owner_phone = models.BigIntegerField()
    rent = models.IntegerField()
    img1 = models.ImageField(default='default_room.jpg', upload_to='room_pics')
    img2 = models.ImageField(default='default_room.jpg', upload_to='room_pics')
    img3 = models.ImageField(default='default_room.jpg', upload_to='room_pics')
    img4 = models.ImageField(default='default_room.jpg', upload_to='room_pics')

    def __str__(self):
        return self.room
