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
    vacancies = Vacancy.objects.all()
    return render(request, 'index.html',
                  context={'vacancies': vacancies})



def add_vacancy(request):

    if request.method == 'POST':
        form = VacancyAddForm(request.POST)

        if form.is_valid():
            add_form = form.save(commit=False)
            print(f'{generate_random_string(10) = }')
            add_form.name = generate_random_string(10)
            add_form.save()
            return redirect('vacancy:index')
    else:
        form = VacancyAddForm()

    return render(request, 'index.html', {'form': form})
