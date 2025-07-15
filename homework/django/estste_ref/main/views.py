from django.shortcuts import render
# from estate.models import Item
# Create your views here.


def index(request):
    # example_item = Item.objects.get(id=1)
    return render(request, 'main\index.html')

