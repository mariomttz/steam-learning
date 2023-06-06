# Libraries and packages
from interfaces.choices import options
from django import forms

# Tags form
class tagsForm(forms.Form):
    first  = forms.ChoiceField(choices = options, required = True, label = 'Tag #1')
    second = forms.ChoiceField(choices = options, required = True, label = 'Tag #2')
    third  = forms.ChoiceField(choices = options, required = True, label = 'Tag #3')
    fourth = forms.ChoiceField(choices = options, required = True, label = 'Tag #4')
    fifth  = forms.ChoiceField(choices = options, required = True, label = 'Tag #5')
    sixth  = forms.ChoiceField(choices = options, required = True, label = 'Tag #6')
    price  = forms.FloatField(min_value = 0.0, required = True, label = 'Precio')