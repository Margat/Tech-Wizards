from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Query', max_length=100)
    min_prince = forms.IntegerField(label='Min Price', min_value=0,)
    max_price = forms.IntegerField(label='Max Price')
