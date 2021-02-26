from django import forms
from django.utils.translation import ugettext_lazy as _

class SearchForm(forms.Form):
    search_field = forms.CharField(label=_("Search term:"), widget=forms.TextInput(
        attrs={
            "placeholder": "Enter search term",
            "class":"form-control border border-dark",
    }))

class CreateNewEntryForm(forms.Form):
    title = forms.CharField(
        label=_("Title:"), 
        max_length=50, 
        widget=forms.TextInput(attrs={
            "class":"form-control border border-dark"
    }))
    markdown_content = forms.CharField(
        label=_("Markdown content:"),
        help_text=_("Please use markdown syntax for entry content"), 
        widget=forms.Textarea(attrs={
            "class":"form-control border border-dark",
    }))