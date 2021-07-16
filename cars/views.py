from django.shortcuts import render, get_object_or_404 , redirect
from .models import Car , Cars , Brand , Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import CarForm
from django.core.files.storage import FileSystemStorage
import os
from accounts.models import Cuspack , Package
from django.contrib import messages, auth

# Create your views here.
def cars(request):
    cars = Cars.objects.order_by('-created_date')
    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    brand_search = Brand.objects.all()

    city_search = Cars.objects.values_list('city',flat=True).distinct()
    year_search = Cars.objects.order_by('year').values_list('year',flat=True).distinct()
    category_search = Category.objects.all()

    data= {
    'cars':paged_cars,
    'brand_search':brand_search,
    'city_search':city_search,
    'year_search':year_search,
    'category_search':category_search,

    }
    return render(request, 'cars/cars.html',data)

def car_detail(request,id):
    single_car = get_object_or_404(Cars , pk=id)
    data = {
    'single_car':single_car,
    }
    return render(request,'cars/car_detail.html',data)

def post(request):
    if request.method == 'POST':
        user = request.user
        car_title = request.POST['car_title']
        brand = request.POST['brand']
        brand = Brand.objects.get(id=brand)
        category = request.POST['category']
        category = Category.objects.get(id=category)
        transmission = request.POST['transmission']
        fuel_type = request.POST['fuel_type']
        model = request.POST['model']
        color = request.POST['color']
        year = request.POST['year']
        price = request.POST['price']
        engine = request.POST['engine']
        description = request.POST['description']
        interior = request.POST['interior']
        mileage = request.POST['mileage']
        km_driven = request.POST['km_driven']
        passengers = request.POST['passengers']
        doors = request.POST['doors']
        features = request.POST.getlist('features')
        featuress = ','.join(features)

        condition = request.POST['condition']
        no_of_owners = request.POST['no_of_owners']
        state = request.POST['state']
        district = request.POST['district']
        city = request.POST['city']
        car_photo = request.FILES['myfile1']


        car_photo_1 = request.FILES['myfile2']
        car_photo_2 = request.FILES['myfile3']
        car_photo_3 = request.FILES['myfile4']
        car_photo_4 = request.FILES['myfile5']
        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        # uploaded_filename = request.FILES['myfile'].name
        # full_filename = os.path.join( 'photos', uploaded_filename)
        # full_filenamee = os.path.join( MEDIA_ROOT,'photos', uploaded_filename)
        cuspack = Cuspack.objects.get(user=user)




        fs = FileSystemStorage()
        fs.save(car_photo.name,car_photo)
        fs.save(car_photo_1.name,car_photo_1)
        fs.save(car_photo_2.name,car_photo_2)
        fs.save(car_photo_3.name,car_photo_3)
        fs.save(car_photo_4.name,car_photo_4)
        # Iterate through the chunks.
        # for chunk in fout.read():
        #     fout.write(chunk)
        #     fout.close()
        if(cuspack.total_cars > 1):
            is_featured = True

        if cuspack.no_of_cars < cuspack.total_cars:


            car = Cars.objects.create(user=user,car_title=car_title,brand=brand,category=category,transmission=transmission,fuel_type=fuel_type,model=model,
            color=color,year=year,price=price,engine=engine,description=description,interior=interior,mileage=mileage,km_driven=km_driven,passengers=passengers,
            doors = doors,no_of_owners=no_of_owners,state=state,district=district,city=city,car_photo=car_photo,car_photo_1=car_photo_1,car_photo_2=car_photo_2,
            car_photo_3=car_photo_3,car_photo_4=car_photo_4,features = featuress,condition=condition)
            cuspack.no_of_cars = cuspack.no_of_cars + 1
            cuspack.save()

        else:
            messages.error(request, 'Sorry Your limit is over please upgrade')


        return redirect('dashboard')

    else:

        features = [
                'Cruise Control',
                'Audio Interface',
                'Airbags',
                'Air Conditioning',
                'Seat Heating',
                'Alarm System',
                'ParkAssist',
                'Power Steering',
                'Reversing Camera',
                'Direct Fuel Injection',
                'Auto Start/Stop',
                'Wind Deflector',
                'Bluetooth Handset'
                    ]
        brands = Brand.objects.all()
        categories = Category.objects.all();
        form = CarForm()
        data = {
        'brands':brands,
        'categories':categories,
        'form':form,
        'features':features,
        }
        return render(request,'cars/post.html',data)



def search(request):
    cars = Cars.objects.order_by('-created_date')
    brand_search = Brand.objects.all()
    transmission_search = Cars.objects.values_list('transmission',flat=True).distinct()
    fuel_search =Cars.objects.values_list('fuel_type',flat=True).distinct()
    city_search = Cars.objects.values_list('city',flat=True).distinct()
    year_search = Cars.objects.order_by('year').values_list('year',flat=True).distinct()
    category_search = Category.objects.all()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains = keyword)

    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            cars = cars.filter(brand__gte = brand , brand__lte = brand)


    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact = year)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            cars = cars.filter(category__gte = category , category__lte = category )


    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact = city)

    if 'fuel' in request.GET:
        fuel = request.GET['fuel']
        if fuel:
            cars = cars.filter(fuel_type__iexact = fuel)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact = transmission)


    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price,price__lte=max_price)


    data = {
        'cars':cars,
        'brand_search':brand_search,
        'city_search':city_search,
        'year_search':year_search,
        'category_search':category_search,
        'fuel_search':fuel_search,
        'transmission_search':transmission_search,
    }
    return render(request,'cars/search.html',data)
