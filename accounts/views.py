from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from .models import Cuspack , Package , Card , Packageorder
from cars.models import Cars
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def report(request):
    if request.method == 'POST':
        fromdate = request.POST['from']
        todate = request.POST['to']
        type = request.POST['type']
        if type == 'car':
            res = Cars.objects.values('created_date').annotate(dcount=Count('created_date')).filter(created_date__lte = todate , created_date__gte = fromdate)

            i = 1
            data = {
                'res': res,
                'i':i,
            }
            return render(request, 'accounts/generate.html',data)

        elif type== 'purchase':
            res = Packageorder.objects.filter(date__lte = todate , date__gte = fromdate)

            i = 1
            data = {
                'res': res,
                'i':i,
            }
            return render(request, 'accounts/generatep.html',data)

        elif type== 'user':
            res = User.objects.filter(date_joined__lte = todate , date_joined__gte = fromdate)

            i = 1
            data = {
                'res': res,
                'i':i,
            }
            return render(request, 'accounts/generateu.html',data)

    else:

        return render(request, 'accounts/report.html')


def generate(request):

    return render(request, 'accounts/generate.html')

def generatep(request):

    return render(request, 'accounts/generatep.html')

def generateu(request):

    return render(request, 'accounts/generateu.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    package = Package.objects.get(id=1)
                    cuspack = Cuspack.objects.create(user = user)
                    cuspack.save()
                    auth.login(request, user)

                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    user = request.user
    cars = Cars.objects.filter(user=user)
    mssg = Contact.objects.filter(ruser_id=user)


    # count = Contact.objects.order_by('-create_date').filter(user_id=request.user.id).count()

    data = {
        'inquiries': user_inquiry,
        'cars':cars ,
        'user':user ,
        'mssg':mssg,

    }
    return render(request, 'accounts/dashboard.html',data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')

def delete(request,id):
    id = id
    car = Cars.objects.get(id=id)
    car.delete()


    return render(request,'accounts/dashboard.html')


def payment(request):
    if request.method == 'GET':
        user = request.user
        id = request.GET['p']
        package = Package.objects.get(id=id)
        cuspack = Cuspack.objects.get(user=user)
        cuspack.total_cars = cuspack.total_cars + package.cars
        cuspack.save()

        packageorder = Packageorder.objects.create(user=user,package=package , price = package.price , status= "successfull")

        data = {
            'packageorder': packageorder,

        }


    return render(request, 'accounts/payment.html',data)

def card(request,id):

    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        number = request.POST['number']
        expiry = request.POST['expiry']
        card = Card.objects.create(user=user,name=name,number=number,expiry=expiry)
        return redirect('/accounts/payment?p=%s' % id)


    else:
        return render(request, 'accounts/card.html')


def packages(request):
    packages = Package.objects.all()

    data = {
        'packages': packages,

    }

    return render(request, 'accounts/packages.html',data)


def delete_event(request,event_id):
    event = Cuspack.objects.get(pk=event_id)
    event.delete()
    return render(request,'accounts/dashboard.html')
