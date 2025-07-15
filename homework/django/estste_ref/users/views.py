from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from users.forms import SignUpForm

# Create your views here.

def signup_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('properties:list')
    else:
        form = SignUpForm()

    return render(request, template_name='signup.html',
                  context={'form': form})