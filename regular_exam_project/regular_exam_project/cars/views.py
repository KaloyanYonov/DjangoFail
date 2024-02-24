from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from regular_exam_project.cars.form import CarForm


def car_catalogue(request):

    cars = Car.objects.all()
    return render(request, 'cars/catalogue.html', {'cars': cars})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('car_details', id=car.id)
    else:
        form = CarForm()
    return render(request, 'cars/car-create.html', {'form': form})

def car_details(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'cars/car-details.html', {'car': car})

def car_edit(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_details', id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car-edit.html', {'form': form, 'car': car})

def car_delete(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        car.delete()
        return redirect('car_catalogue')
    return render(request, 'cars/car-delete.html', {'car': car})
