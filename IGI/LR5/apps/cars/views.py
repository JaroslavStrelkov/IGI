from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Car, Manufacturer, CarCategory, Feature
from apps.accounts.utils import (employee_required)
import logging
logger = logging.getLogger(__name__)

def cars_list(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    category = request.GET.get('category')
    manufacturer = request.GET.get('manufacturer')
    sort = request.GET.get('sort')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if search:
        cars = cars.filter(name__icontains=search)
    if category:
        cars = cars.filter(category_id=category)

    if manufacturer:
        cars = cars.filter(manufacturer_id=manufacturer)

    if min_price:
        cars = cars.filter(price__gte=min_price)

    if max_price:
        cars = cars.filter(price__lte=max_price)

    if sort == 'price_asc':
        cars = cars.order_by('price')

    elif sort == 'price_desc':
        cars = cars.order_by('-price')

    elif sort == 'year_asc':
        cars = cars.order_by('year')

    elif sort == 'year_desc':
        cars = cars.order_by('-year')

    categories = CarCategory.objects.all()
    manufacturers = Manufacturer.objects.all()

    return render(request, 'cars/index.html', {'cars': cars, 'categories': categories, 'manufacturers': manufacturers,})

@employee_required
def create_car(request):
    if request.method == 'POST':
        car = Car()
        car.name = request.POST.get('name')
        car.description = request.POST.get('description')
        car.price = request.POST.get('price')
        car.year = request.POST.get('year')
        car.mileage = request.POST.get('mileage')
        car.transmission = request.POST.get('transmission')
        car.fuel_type = request.POST.get('fuel_type')
        car.is_available = bool(request.POST.get('is_available'))
        category_id = request.POST.get('category')
        manufacturer_id = request.POST.get('manufacturer')
        car.category = CarCategory.objects.get(id=category_id)
        car.manufacturer = Manufacturer.objects.get(id=manufacturer_id)

        if 'image' in request.FILES:
            car.image = request.FILES['image']

        logger.info(f'Car is created: {car.name}')

        car.save()

        features = request.POST.getlist('features')
        car.features.set(features)

        return HttpResponseRedirect('/cars/')

    categories = CarCategory.objects.all()
    manufacturers = Manufacturer.objects.all()
    features = Feature.objects.all()

    return render(request, 'cars/create.html', {'categories': categories, 'manufacturers': manufacturers, 'features': features,})


@employee_required
def edit_car(request, id):

    try:
        car = Car.objects.get(id=id)

        if request.method == 'POST':
            car.name = request.POST.get('name')
            car.description = request.POST.get('description')
            car.price = request.POST.get('price')
            car.year = request.POST.get('year')
            car.mileage = request.POST.get('mileage')
            car.transmission = request.POST.get('transmission')
            car.fuel_type = request.POST.get('fuel_type')
            car.is_available = bool(request.POST.get('is_available'))
            category_id = request.POST.get('category')
            manufacturer_id = request.POST.get('manufacturer')
            car.category = CarCategory.objects.get(id=category_id)
            car.manufacturer = Manufacturer.objects.get(id=manufacturer_id)

            if 'image' in request.FILES:
                car.image = request.FILES['image']

            logger.info(f'Car is edit: {car.name}, arbeiter: {request.user.username}')

            car.save()

            features = request.POST.getlist('features')
            car.features.set(features)

            return HttpResponseRedirect('/cars/')

        categories = CarCategory.objects.all()
        manufacturers = Manufacturer.objects.all()
        features = Feature.objects.all()

        return render(request, 'cars/edit.html', {'car': car, 'categories': categories, 'manufacturers': manufacturers, 'features': features,})

    except Car.DoesNotExist:
        return HttpResponseNotFound('<h2>Car not found</h2>')


@employee_required
def delete_car(request, id):

    try:
        car = Car.objects.get(id=id)
        car.delete()
        logger.warning(f'Car is delete: {car.name}')

        return HttpResponseRedirect('/cars/')
    
    except Car.DoesNotExist:

        return HttpResponseNotFound('<h2>Car not found</h2>')
