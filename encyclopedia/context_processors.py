from . import forms

def add_search_form(request):
    return {
        "search_form": forms.SearchForm()
    }