from django.db import models

# Create your models here.


DropOffto = (
    ("watchman", "watchman"),
    ("Padosi", "Padosi"),
    ("mailbox", "mailbox"),
    
)


weightrate = (
    ("10", "10"),
    ("20", "20"),
    
)

Postal_rate = (
    ("10", "10"),
    ("20", "20"),
    
)

typeofdel = (
    ("paper", "paper"),
    ("parcel", "parcel"),
)




class Single(models.Model):
    From = models.CharField(max_length=255)
    To = models.CharField(max_length=255)
    #location = PlainLocationField(based_fields=['city'], zoom=7)
    typeofdel = models.CharField(max_length=255, choices=typeofdel)
    Dropoffto = models.CharField(max_length=255, choices=DropOffto)
    pin_no = models.IntegerField(max_length=255)
    Full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    Flat_number_and_building_name = models.CharField(max_length=255)
    Area = models.CharField(max_length=255)
    Land_mark = models.CharField(max_length=255)
    weightrate = models.CharField(max_length=255, choices=weightrate)
    Describe_del = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    #Image = models.FileField(upload_to='products/images/', null= True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.typeofdel


class Multiple(models.Model):
    From = models.CharField(max_length=255)
    To = models.CharField(max_length=255)
    #location = PlainLocationField(based_fields=['city'], zoom=7)
    typeofdel = models.CharField(max_length=255, choices=typeofdel)
    Dropoffto = models.CharField(max_length=255, choices=DropOffto)
    pin_no = models.IntegerField(max_length=255)
    Full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    Flat_number_and_building_name = models.CharField(max_length=255)
    Area = models.CharField(max_length=255)
    Land_mark = models.CharField(max_length=255)
    weightrate = models.CharField(max_length=255, choices=weightrate)
    Describe_del = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    #Image = models.FileField(upload_to='products/images/', null= True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.typeofdel


class Postal(models.Model):
    From = models.CharField(max_length=255)
    To = models.CharField(max_length=255)
    #location = PlainLocationField(based_fields=['city'], zoom=7)
    typeofdel = models.CharField(max_length=255, choices=typeofdel)
    Dropoffto = models.CharField(max_length=255, choices=DropOffto)
    pin_no = models.IntegerField(max_length=255)
    Full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    Flat_number_and_building_name = models.CharField(max_length=255)
    Area = models.CharField(max_length=255)
    Land_mark = models.CharField(max_length=255)
    weightrate = models.CharField(max_length=255, choices=weightrate)
    Describe_del = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    #Image = models.FileField(upload_to='products/images/', null= True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.typeofdel


class Postal(models.Model):
    From = models.CharField(max_length=255)
    To = models.CharField(max_length=255)
    typeofdel = models.CharField(max_length=255, choices=typeofdel)
    del_pin_no = models.IntegerField(max_length=255)
    Full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    Flat_number_and_building_name = models.CharField(max_length=255)
    Area = models.CharField(max_length=255)
    Land_mark = models.CharField(max_length=255)
    Postal_rate = models.CharField(max_length=255, choices=Postal_rate)
    weightrate = models.CharField(max_length=255, choices=weightrate)
    Describe_del = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    #Image = models.FileField(upload_to='products/images/', null= True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.typeofdel