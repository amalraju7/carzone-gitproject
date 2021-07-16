from django.shortcuts import render, redirect
from .models import Team , Feedback
from cars.models import Car , Cars , Brand , Category
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = Cars.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Cars.objects.order_by('-created_date')
    brand_search = Brand.objects.all()

    city_search = Cars.objects.values_list('city',flat=True).distinct()
    year_search = Cars.objects.values_list('year',flat=True).distinct()
    category_search = Category.objects.all()
    data = {
        'teams': teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'brand_search':brand_search,
        'city_search':city_search,
        'year_search':year_search,
        'category_search':category_search,

    }
    return render(request, 'pages/home.html',data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':

        subject = request.POST['subject']
        user = request.user
        message = request.POST['message']

        feedback = Feedback.objects.create(user=user,subject=subject,feedback=message)



        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')
