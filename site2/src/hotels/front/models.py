from django.db import models

# Create your models here.

class Hotel(models.Model):
    
    short_name = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    stars = models.IntegerField(default=3)
    desc_1 = models.CharField(max_length=255)
    title_1 = models.CharField(max_length=255)
    desc_2 = models.CharField(max_length=255, null=True, blank=True)
    title_2 = models.CharField(max_length=255, null=True, blank=True)
    desc_3 = models.CharField(max_length=255, null=True, blank=True)
    title_3 = models.CharField(max_length=255, null=True, blank=True)
    img_1 = models.ImageField(upload_to="hotels")
    img_2 = models.ImageField(upload_to="hotels", null=True, blank=True)
    img_3 = models.ImageField(upload_to="hotels", null=True, blank=True)
    about_us = models.CharField(max_length=255)
    years = models.IntegerField(default=2)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(default=0, null=True, blank=True)
    longitude = models.FloatField(default=0, null=True, blank=True)
    number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    
    ROM_TYPES = [('Single', 'Single'),
                 ('Double', 'Double'),
                 ('Suit', 'Suit')]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    rom_type = models.CharField(max_length=255, choices=ROM_TYPES)
    start_date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    end_time = models.TimeField(auto_now_add=True)
    guests = models.IntegerField(default=1)
    hotel = models.ForeignKey(Hotel, models.CASCADE, related_name='reservations')
    
    
class Gallery(models.Model):
    
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=1000)
    image = models.ImageField(upload_to="gallery")
    hotel = models.ForeignKey(Hotel, models.CASCADE, related_name='galleries')
