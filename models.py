from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tour_cat(models.Model):
    Cat_name=models.CharField(max_length=20)

    def __str__(self):
        return self.Cat_name


class Tour(models.Model):
    Category_name = models.ForeignKey(Tour_cat,on_delete=models.CASCADE,related_name='tours')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations')
    price = models.IntegerField()
    rating = models.PositiveIntegerField(default='1')
    duration = models.CharField(max_length=50, default="2 days 3 nights")
    location = models.CharField(max_length=100)

class Hotel(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations')
    price = models.IntegerField()
    rating = models.PositiveIntegerField(default='1')
    location = models.CharField(max_length=100)


class Contact(models.Model):
    message = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    name = models.CharField(max_length=200)

class Information(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')

class Hotel_info(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price = models.IntegerField()

class Tour_booking(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    Tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    # date = models.DateField()
    destination = models.CharField(max_length=50)
    no_person = models.IntegerField(default=1)
    price = models.IntegerField()
    t_price = models.IntegerField()
    duration = models.CharField(max_length=100)
    is_booking = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'),
                                                              ('Failed', 'Failed')], default='Pending')

class Hotel_booking(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    checkin = models.DateField()
    checkout = models.DateField()
    no_guest = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    message = models.CharField(max_length=250)
    is_booking = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'),
                                                              ('Failed', 'Failed')], default='Pending')

