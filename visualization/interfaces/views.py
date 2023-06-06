# Libraries and packages
from django.shortcuts import render, redirect
from interfaces.forms import tagsForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        pass

    else:
        form = tagsForm()
        return render(request, 'index.html', {'form': form})

