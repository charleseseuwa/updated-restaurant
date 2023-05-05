from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact, Booking, Service, Menu, Subscriber, Member


# Create your views here.
def about_page(request):
    return render(request, 'content/about.html')

def service_page(request):
    return render(request, 'content/service.html')

def testimonial_page(request):
    return render(request, 'content/testimonial.html')

def team_page(request):
    return render(request, 'content/team.html')

def index_page(request):
        if request.method == "POST":
            booking_name = request.POST.get("name")
            booking_email = request.POST.get("email")
            booking_select = request.POST.get("select")
            booking_message = request.POST.get("message")
            Booking.objects.create(name=booking_name, email=booking_email, select=booking_select, message=booking_message )

            return HttpResponse("Thanks for booking, order will be processed shortly")
    
        all_services = Service.objects.all()
        all_menu = Menu.objects.all()
        all_member = Member.objects.all()

        context = {

                'all_services' : all_services,
                'all_items' : all_menu,
                'all_member' : all_member
            }
             
        return render(request, 'content/index.html', context)

def menu_page(request):
    return render(request, 'content/menu.html')

def contact_page(request):
    if request.method == 'GET':
        return render(request, 'content/contact.html')
    
    elif request.method == 'POST':
        
        new_contact_name = request.POST.get("name")
        new_contact_email = request.POST.get("email")
        new_contact_subject = request.POST.get("subject")
        new_contact_message = request.POST.get("message")
        
        Contact.objects.create(name=new_contact_name, email=new_contact_email, subject =new_contact_subject, message=new_contact_message  )

        return HttpResponse("Your message has been sent")
    
    elif request.method == 'POST':
    
        newsletter = request.POST.get("email")
        Subscriber.objects.create(email=newsletter)
        return HttpResponse("Your message has been sent")


    

def booking_page(request):
    if request.method == "POST":
        booking_name = request.POST.get("name")
        booking_email = request.POST.get("email")
        booking_select = request.POST.get("select")
        booking_message = request.POST.get("message")

        Booking.objects.create(name=booking_name, email=booking_email, select=booking_select, message=booking_message )

        return HttpResponse("Thanks for booking, order will be processed shortly")
    if request.method == 'POST':
    
        newsletter = request.POST.get("email")
        Subscriber.objects.create(email=newsletter)
        return HttpResponse("Your message has been sent")
    else:
        return render(request, 'content/booking.html')