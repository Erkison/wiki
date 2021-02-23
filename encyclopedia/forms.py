from django import forms

class SearchForm(forms.Form):
    search_field = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Search"}))

class CreateNewEntryForm(forms.Form):
    title = forms.CharField(max_length=50)
    markdown_content = forms.CharField()