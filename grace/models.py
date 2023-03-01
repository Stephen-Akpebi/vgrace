from django.db import models

# Create your models here.
# Developed by Surfa
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from rest_framework import serializers
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"publish")
)


class Sermon(models.Model):
    title = models.CharField(max_length=200, unique=False)
    date = models.DateTimeField(auto_now=True)
    video_link = models.URLField( max_length=500)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=False)
    
    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image2 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image3 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image4 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image5 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image6 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title



class Event_Gallery(models.Model):
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=200, unique=True)
    image2 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title2 = models.CharField(max_length=200, unique=True)
    image3 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title3 = models.CharField(max_length=200, unique=True)
    image4 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title4 = models.CharField(max_length=200, unique=True)
    image5 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title5 = models.CharField(max_length=200, unique=True)
    image6 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title6 = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title



class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    message = models.TextField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    link = models.URLField( max_length=200)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Charity(models.Model):
    name = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    amount = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

class Pastors(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    position = models.CharField(max_length=200, unique=True)
    fb_account = models.CharField(max_length=200, unique=True)
    twitter_account = models.CharField(max_length=200, unique=True)
    ig_account = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    message = models.TextField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

User = get_user_model()



class Podcasts(models.Model):
    audio_file = models.FileField(upload_to='audio/%Y/%m/%d/', null=True, blank=True)
    audio_image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Sermon_main(models.Model):
    title = models.CharField(max_length=200, unique=False)
    date = models.DateTimeField(auto_now=True)
    video_link = models.URLField( max_length=500)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=False)
    
    def __str__(self):
        return self.title


class Gallery_main(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image2 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image3 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image4 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image5 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    image6 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title



class Event_Gallery_main(models.Model):
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=200, unique=True)
    image2 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title2 = models.CharField(max_length=200, unique=True)
    image3 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title3 = models.CharField(max_length=200, unique=True)
    image4 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title4 = models.CharField(max_length=200, unique=True)
    image5 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title5 = models.CharField(max_length=200, unique=True)
    image6 = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title6 = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title



class Event_main(models.Model):
    title = models.CharField(max_length=200, unique=True)
    message = models.TextField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    link = models.URLField( max_length=200)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title



class Pastors_main(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    position = models.CharField(max_length=200, unique=True)
    fb_account = models.CharField(max_length=200, unique=True)
    twitter_account = models.CharField(max_length=200, unique=True)
    ig_account = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name




class Podcasts_main(models.Model):
    audio_file = models.FileField(upload_to='audio/%Y/%m/%d/', null=True, blank=True)
    audio_image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
