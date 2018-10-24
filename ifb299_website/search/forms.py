from django import forms
from django.core.exceptions import ValidationError

year_choices = [('Blank', '')]
sort_choices = [('ASC', 'Price Ascending'), ('DESC', 'Price Descending')]
for x in range(1900,2019):
    year_choices.append((x,x))

class SearchForm(forms.Form):
	query = forms.CharField(label='Search', max_length=100, required=False)
	min_price = forms.IntegerField(label='Min Price', min_value=0, max_value=9999999, required=False)
	max_price = forms.IntegerField(label='Max Price', min_value=0, max_value=9999999, required=False)
	year = forms.ChoiceField(label='Year', choices=year_choices, required=False)
	sort = forms.ChoiceField(label='Sort', choices=sort_choices, required=False)
	