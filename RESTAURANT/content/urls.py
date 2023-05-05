from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name= 'index'),
    path('contact.html/', contact_page, name='contact'),
    path('booking.html/', booking_page, name='booking'),
    path('about.html/', about_page, name='about'),
    path('service.html/', service_page, name='service'),
    path('team.html/', team_page, name='team'),
    path('testimonial.html/', testimonial_page, name='testimonial'),
    path('menu.html/', menu_page, name='menu')
    ]