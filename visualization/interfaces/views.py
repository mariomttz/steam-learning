# Libraries and packages
from interfaces.functions import csv_pred_creator, rating_converter
from django.shortcuts import render, redirect
from interfaces.forms import tagsForm
from time import sleep

# Main view
def index(request):
    if request.method == 'POST':
        form = tagsForm(request.POST)

        if form.is_valid():
            numberTags = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
            tags = set([form.cleaned_data[numberTag] for numberTag in numberTags])

            if len(tags) == 6:
                price = form.cleaned_data['price']
                csv_pred_creator(price, tags)

                # We put the program to sleep, to load the information
                sleep(1)

                # We declare the route
                PATH = '../processing/dataset/'

                # We read the file with the qualification
                with open(PATH + 'rating.txt', 'r+') as f:
                    qualification = int(f.read())

                rating = rating_converter(qualification)
                return render(request, 'rating.html', {'tags': tags, 'price': price, 'rating': rating})

            else:
                fieldNames = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'price']
                initial_data = {fieldName: form.cleaned_data[fieldName] for fieldName in fieldNames}
                form = tagsForm(initial = initial_data)
                error = 'No puedes repetir tags, por favor, inténtalo de nuevo.'
                return render(request, 'index.html', {'form': form, 'error': error})

        else:
            fieldNames = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'price']
            initial_data = {fieldName: form.cleaned_data[fieldName] for fieldName in fieldNames}
            form = tagsForm(initial = initial_data)
            error = 'Ha ocurrido un error al enviar el formulario, por favor, inténtalo de nuevo.'
            return render(request, 'index.html', {'form': form, 'error': error})

    else:
        initial_data = {'first': 'Action', 'second': 'Adventure', 'third': 'Singleplayer',
                        'fourth': 'Casual', 'fifth': 'Strategy', 'sixth': 'Simulation',
                        'price': 0.0}
        form = tagsForm(initial = initial_data)
        return render(request, 'index.html', {'form': form})
