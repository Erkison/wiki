from django import forms

class SearchForm(forms.Form):
    search_field = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Search"}))