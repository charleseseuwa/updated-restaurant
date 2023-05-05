from django.db import models
import datetime
# Create your models here.

        
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
SUBJECT_CHOICES = (
    ("select1", "select1"),
    ("select2", "select2"),
    ("select3", "select3")
)
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    datetime = models.DateField(blank=True, null=True,default=datetime.date.today)
    select = models.CharField(choices=SUBJECT_CHOICES, max_length=7)

    def __str__(self):
        return self.name
    

class Member(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images')
    price = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.name

class social(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='socials.image')

    def __str__(self):
        return self.name