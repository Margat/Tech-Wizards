from django import forms
CHOICES = (('0', 'None'), ('1', '1981'), ('2', '1982'), ('3', '1983'),
           ('4', '1984'), ('5', '1985'), ('6', '1986'), ('7', '1987'),
           ('8', '1988'), ('9', '1989'), ('10', '1990'), ('11', '1992'),
           ('12', '1993'),('13', '1994'), ('14', '1995'), ('15', '1996'), 
           ('16', '1997'),('17', '1998'), ('18', '1999'), ('19', '2000'), 
           ('20', '2001'), ('21', '2002'), ('22', '2003'), ('23', '2004'),
           ('24', '2004'), ('25', '2005'), ('26', '2006'), ('26', '2007'))
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)
    min_price = forms.IntegerField(label='Min Price', min_value=0,required=False)
    max_price = forms.IntegerField(label='Max Price',required=False)
    year = forms.ChoiceField(choices=CHOICES)
