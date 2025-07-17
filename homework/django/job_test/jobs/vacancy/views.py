from django.shortcuts import render, redirect
from vacancy.models import Vacancy
from vacancy.forms import VacancyAddForm, VacancyRemoveForm, VacancyShowForm
import random
import string

def generate_random_string(length):
    """Generates a random string of specified length using letters and digits."""
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string


def index(request):
    # items = Vacancy.objects.get(id=1)
    vacancies = Vacancy.objects.all()
    return render(request, 'index.html',
                  context={'vacancies': vacancies})


def add(request):

    if request.method == 'POST':
        form = VacancyAddForm(request.POST)

        if form.is_valid():
            add_form = form.save(commit=False)
            add_form.name = generate_random_string(10)
            add_form.save()
            return redirect('vacancy:index')
    else:
        form = VacancyAddForm()

    return render(request, 'index.html', {'form': form})


def remove(request):

    if request.method == 'POST':
        form = VacancyRemoveForm(request.POST)
        id_to_delete = request.POST.get('id')

        if form.is_valid():
            del_form = form.save(commit=False)
            if id_to_delete and id_to_delete.isdigit():
                Vacancy.objects.filter(pk=int(id_to_delete)).delete()
            del_form.save()
            return redirect('vacancy:index')
    else:
        form = VacancyAddForm()

    return render(request, 'index.html', {'form': form})

def show(request):

    if request.method == 'POST':
        form = VacancyRemoveForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('vacancy:index')
    else:
        form = VacancyAddForm()

    return render(request, 'index.html', {'form': form})

