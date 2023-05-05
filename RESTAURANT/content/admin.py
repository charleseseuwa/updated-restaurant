from django.contrib import admin
from .models import Contact, Booking, Member, Menu, Subscriber, Service
admin.site.register([Contact, Booking, Member, Menu, Subscriber, Service])

