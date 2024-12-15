from django.shortcuts import render
from .models import Person  # Import Person model

# View to display the homepage
def home(request):
    return render(request, 'myapp/home.html')

# View to display the list of persons
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'myapp/person_list.html', {'persons': persons})
