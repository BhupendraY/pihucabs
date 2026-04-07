from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse

def user_list(request):
    return render(request, "index.html")

from django.shortcuts import render, redirect
from .models import Booking

from django.shortcuts import render
from django.contrib import messages
from .models import Booking
from django.core.mail import send_mail

def user_list(request):
    return render(request, "index.html")

def book_taxi(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        passengers = request.POST.get('passengers')
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')
        date = request.POST.get('date')
        time = request.POST.get('time')

        Booking.objects.create(
            name=name,
            phone=phone,
            passengers=passengers,
            from_location=from_location,
            to_location=to_location,
            date=date,
            time=time
        )
        
         # 📧 Email Message
        subject = "New Taxi Booking"
        message = f"""
                New Booking Details 🚖

                Name: {name}
                Phone: {phone}
                Passengers: {passengers}
                From: {from_location}
                To: {to_location}
                Date: {date}
                Time: {time}
        """

        from_email = 'yourgmail@gmail.com'
        recipient_list = ['bsyadav9410@gmail.com','rajy0707@gmail.com','akkiyadavbaleni@gmail.com']  # 👈 jahan mail receive karna hai

        send_mail(subject, message, from_email, recipient_list)

        messages.success(request, "Booking submitted successfully. We will call you shortly.")

    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

